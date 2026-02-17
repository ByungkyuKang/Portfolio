import os

def move_dir_chk_img(dir_in):
    """
    Move to directory, return list of image file names in that directory.
    (Keep behavior: chdir + return filenames)
    """
    try:
        os.chdir(dir_in)
    except Exception:
        print("The directory you entered does not exist. Please check the path and try again.")
        raise SystemExit(1)
    else:
        print(f'Directory "{dir_in}" exists.')

    image_extensions = ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp')
    image_files = [f for f in os.listdir(dir_in) if f.lower().endswith(image_extensions)]

    if image_files:
        print(f"{len(image_files)} image(s) exist(s) in the directory.")
    else:
        print("No images found in the directory. Exiting the program.")
        raise SystemExit(0)

    return image_files
