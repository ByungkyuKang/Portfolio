from __future__ import annotations
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor
from PIL import Image
import imagehash

# -----------------------------
# Union-Find (Disjoint Set)
# -----------------------------
class DSU:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x: int) -> int:
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a: int, b: int) -> None:
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return
        if self.rank[ra] < self.rank[rb]:
            self.parent[ra] = rb
        elif self.rank[ra] > self.rank[rb]:
            self.parent[rb] = ra
        else:
            self.parent[rb] = ra
            self.rank[ra] += 1


def _compute_phash(filename: str, hash_size: int) -> tuple[str, imagehash.ImageHash] | None:
    """
    Compute pHash once per image.
    NOTE: image files are in current working directory (img_directory does chdir()).
    """
    try:
        with Image.open(filename) as im:
            im = im.convert("RGB")
            h = imagehash.phash(im, hash_size=hash_size)
        return filename, h
    except Exception:
        # unreadable/corrupt image -> skip
        return None


def _make_band_keys(h: imagehash.ImageHash, bands: int) -> list[str]:
    """
    LSH-like keys: split hex string of hash into bands.
    More bands => higher recall (more candidates), slightly slower.
    """
    hexstr = str(h)  # stable representation
    chunk_len = max(1, len(hexstr) // bands)
    keys = []
    for i in range(bands):
        start = i * chunk_len
        end = len(hexstr) if i == bands - 1 else (i + 1) * chunk_len
        keys.append(f"{i}:{hexstr[start:end]}")
    return keys


def group_similar_images(
    img_list: list[str],
    *,
    # for "similar images" (resize/brightness) use larger hash and a looser threshold
    hash_size: int = 16,       # 16 => 256-bit hash
    dist_threshold: int = 12,  # looser to catch resized/brightness-changed images
    bands: int = 6,            # more bands => more candidate recall
    max_bucket_size: int = 300,
    workers: int = 8,
) -> list[list[str]]:
    """
    Returns list of groups, each group is list of filenames.
    Fast approach:
      1) compute phash once per image
      2) bucket by band keys
      3) compare only within bucket candidates using Hamming distance
      4) union-find to form groups
    """
    if not img_list:
        return []

    # 1) precompute hashes (parallel)
    results: list[tuple[str, imagehash.ImageHash]] = []
    with ThreadPoolExecutor(max_workers=workers) as ex:
        for out in ex.map(lambda f: _compute_phash(f, hash_size), img_list):
            if out is not None:
                results.append(out)

    if not results:
        return []

    files = [f for f, _ in results]
    hashes = [h for _, h in results]
    n = len(files)

    # 2) bucketing
    buckets: dict[str, list[int]] = defaultdict(list)
    for i, h in enumerate(hashes):
        for key in _make_band_keys(h, bands=bands):
            buckets[key].append(i)

    # 3) compare only candidates
    dsu = DSU(n)
    seen_pairs = set()

    for key, idxs in buckets.items():
        if len(idxs) > max_bucket_size:
            # huge bucket -> skip to avoid explosion (usually low-value)
            continue

        idxs = sorted(idxs)
        for a_pos in range(len(idxs)):
            a = idxs[a_pos]
            for b_pos in range(a_pos + 1, len(idxs)):
                b = idxs[b_pos]
                pair = (a, b)
                if pair in seen_pairs:
                    continue
                seen_pairs.add(pair)

                # imagehash supports subtraction as Hamming distance
                if (hashes[a] - hashes[b]) <= dist_threshold:
                    dsu.union(a, b)

    # 4) collect groups
    grouped: dict[int, list[str]] = defaultdict(list)
    for i, f in enumerate(files):
        root = dsu.find(i)
        grouped[root].append(f)

    groups = list(grouped.values())
    # sort for stable output: bigger groups first, then name
    groups.sort(key=lambda g: (-len(g), g[0].lower()))
    # sort inside each group for stable renaming
    for g in groups:
        g.sort(key=lambda x: x.lower())

    return groups