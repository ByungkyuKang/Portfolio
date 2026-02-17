import os

def name_change(sorted_list):
    """
    sorted_list: list of (filename, group_number)
    Renames files by prefixing group tag like [001]filename.ext

    Uses 2-pass rename to avoid name collisions.
    """
    if not sorted_list:
        return

    # find width
    max_num = max(num for _, num in sorted_list)
    width = len(str(max_num))

    pid = os.getpid()

    # 1) temp rename
    temp_entries = []
    for fname, grp in sorted_list:
        tmp = f"__TMP__{pid}__{fname}"
        os.rename(fname, tmp)
        temp_entries.append((tmp, fname, grp))

    # 2) final rename
    for tmp, orig, grp in temp_entries:
        tag = f"[{grp:0{width}d}]"
        final = f"{tag}{orig}"
        os.rename(tmp, final)
