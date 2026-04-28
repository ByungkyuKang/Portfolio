import os


def move_dir_chk_img(dir_in):
    """
    Function to get all image files in the selected folder

    Parameters:
        dir_in (str): Directory path

    Returns:
        list[str]: List of full image file paths
    """
    if not os.path.isdir(dir_in):
        print("The directory you entered does not exist. Please check the path and try again.")
        return []

    print(f'Directory "{dir_in}" exists.')

    image_extensions = ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp')
    image_files = []

    for f in os.listdir(dir_in):
        full_path = os.path.join(dir_in, f)

        if os.path.isfile(full_path) and f.lower().endswith(image_extensions):
            image_files.append(full_path)

    if image_files:
        print(f"{len(image_files)} image(s) exist(s) in the directory.")
    else:
        print("No images found in the directory. Exiting the program.")

    return image_files