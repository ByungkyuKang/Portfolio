import img_comp as imgc
import img_name_change as inc

def image_process(img_list):
    """
    New fast pipeline:
      1) group by pHash (includes similar images)
      2) assign group numbers
      3) rename with prefix
    """
    # (2) Recommended parameters for grouping visually similar images
    # - dist_threshold: Tune between 10–14 (higher values increase recall 
    #   but may group less similar images)
    # - bands: Around 6 helps reduce missed matches while keeping performance
    #   reasonable
    groups = imgc.group_similar_images(
        img_list,
        hash_size=16,
        dist_threshold=12,
        bands=6,
        max_bucket_size=300,
        workers=8,
    )

    # Assign group IDs and ensure unmatched files are handled as individual
    # groups. In case a file was excluded due to a hash computation error,
    # it is explicitly added as a standalone group.
    grouped_set = set()
    for g in groups:
        grouped_set.update(g)
    missing = [f for f in img_list if f not in grouped_set]
    for f in missing:
        groups.append([f])

    # group id mapping
    img_name_dict = {}
    group_id = 1
    for g in groups:
        for fname in g:
            img_name_dict[fname] = group_id
        group_id += 1

    sorted_dict_by_number = sorted(img_name_dict.items(), key=lambda item: (item[1], item[0].lower()))
    inc.name_change(sorted_dict_by_number)
