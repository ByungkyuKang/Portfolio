import os
import hashlib
import cv2
import imagehash
from PIL import Image
from multiprocessing import Pool, cpu_count


def _file_md5(path, chunk_size=1024 * 1024):
    try:
        md5 = hashlib.md5()

        with open(path, "rb") as f:
            while True:
                chunk = f.read(chunk_size)
                if not chunk:
                    break
                md5.update(chunk)

        return md5.hexdigest()
    except Exception:
        return None


def _safe_image_info(path):
    try:
        file_size = os.path.getsize(path)

        with Image.open(path) as pil_img:
            pil_rgb = pil_img.convert("RGB")
            width, height = pil_rgb.size
            phash_val = imagehash.phash(pil_rgb)

        md5_val = _file_md5(path)

        return {
            "filename": os.path.basename(path),
            "path": path,
            "size": (width, height),
            "file_size": file_size,
            "phash": phash_val,
            "md5": md5_val,
        }

    except Exception as e:
        print(f"Failed to load {path}: {e}")
        return None


def _compare_chunk(args):
    (
        index,
        valid_paths,
        meta,
        hash_distance_threshold,
        use_orb_for_near_hash,
        orb_match_threshold,
    ) = args

    unions = []
    path1 = valid_paths[index]
    info1 = meta[path1]
    hash1 = info1["phash"]

    orb_cache = {}

    def get_orb_desc(path):
        if path in orb_cache:
            return orb_cache[path]

        try:
            gray = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
            if gray is None:
                orb_cache[path] = None
                return None

            orb = cv2.ORB_create()
            _, desc = orb.detectAndCompute(gray, None)
            orb_cache[path] = desc
            return desc

        except Exception:
            orb_cache[path] = None
            return None

    for j in range(index + 1, len(valid_paths)):
        path2 = valid_paths[j]
        info2 = meta[path2]
        hash2 = info2["phash"]

        if info1["md5"] is not None and info1["md5"] == info2["md5"]:
            unions.append((path1, path2))
            continue

        w1, h1 = info1["size"]
        w2, h2 = info2["size"]

        pixels1 = w1 * h1
        pixels2 = w2 * h2

        if max(pixels1, pixels2) > min(pixels1, pixels2) * 4:
            continue

        fs1 = info1["file_size"]
        fs2 = info2["file_size"]

        if max(fs1, fs2) > min(fs1, fs2) * 6:
            continue

        distance = hash1 - hash2

        if distance == 0:
            unions.append((path1, path2))
            continue

        if distance > hash_distance_threshold:
            continue

        if use_orb_for_near_hash:
            desc1 = get_orb_desc(path1)
            desc2 = get_orb_desc(path2)

            if desc1 is None or desc2 is None:
                if distance <= max(1, hash_distance_threshold // 2):
                    unions.append((path1, path2))
                continue

            try:
                matcher = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
                matches = matcher.match(desc1, desc2)

                if len(matches) >= orb_match_threshold:
                    unions.append((path1, path2))

            except Exception:
                if distance <= max(1, hash_distance_threshold // 2):
                    unions.append((path1, path2))
        else:
            unions.append((path1, path2))

    return unions


class UnionFind:
    def __init__(self, items):
        self.parent = {item: item for item in items}
        self.rank = {item: 0 for item in items}

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a, b):
        ra = self.find(a)
        rb = self.find(b)

        if ra == rb:
            return

        if self.rank[ra] < self.rank[rb]:
            self.parent[ra] = rb
        elif self.rank[ra] > self.rank[rb]:
            self.parent[rb] = ra
        else:
            self.parent[rb] = ra
            self.rank[ra] += 1


class ImageComparator:
    def __init__(
        self,
        img_list,
        hash_distance_threshold=6,
        use_orb_for_near_hash=True,
        orb_match_threshold=40,
    ):
        self.img_list = img_list
        self.hash_distance_threshold = hash_distance_threshold
        self.use_orb_for_near_hash = use_orb_for_near_hash
        self.orb_match_threshold = orb_match_threshold
        self.meta = {}

    def preload(self, progress_callback=None):
        total = len(self.img_list)

        for idx, path in enumerate(self.img_list, start=1):
            info = _safe_image_info(path)

            if info is not None:
                self.meta[path] = info

            if progress_callback is not None:
                progress_callback("Loading images...", idx, total)

    def group_duplicates(self, progress_callback=None):
        self.preload(progress_callback=progress_callback)

        valid_paths = list(self.meta.keys())
        uf = UnionFind(valid_paths)

        total_compare_jobs = len(valid_paths)

        if total_compare_jobs == 0:
            return [], [], self.meta

        worker_count = max(1, min(cpu_count(), 6))

        tasks = [
            (
                i,
                valid_paths,
                self.meta,
                self.hash_distance_threshold,
                self.use_orb_for_near_hash,
                self.orb_match_threshold,
            )
            for i in range(len(valid_paths))
        ]

        all_unions = []

        with Pool(processes=worker_count) as pool:
            for idx, unions in enumerate(pool.imap_unordered(_compare_chunk, tasks), start=1):
                all_unions.extend(unions)

                if progress_callback is not None:
                    progress_callback("Comparing images...", idx, total_compare_jobs)

        for a, b in all_unions:
            uf.union(a, b)

        grouped = {}
        for path in valid_paths:
            root = uf.find(path)
            grouped.setdefault(root, []).append(path)

        groups = list(grouped.values())

        for g in groups:
            g.sort(key=lambda p: os.path.basename(p).lower())

        groups.sort(key=lambda g: (-len(g), os.path.basename(g[0]).lower()))

        duplicate_groups = [g for g in groups if len(g) > 1]
        singleton_groups = [g for g in groups if len(g) == 1]

        return duplicate_groups, singleton_groups, self.meta