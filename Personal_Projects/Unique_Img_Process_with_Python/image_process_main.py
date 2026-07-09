import img_processing as imgp
import img_directory as ds
import tkinter as tk
from tkinter import filedialog, messagebox
from multiprocessing import freeze_support

def main():
    """
    main

    order:
    1. Create the Tkinter root window
    2. Select a directory
    3. Collect images
    4. Analyze images and display panels
    5. Run the Tkinter event loop
    """
    root = tk.Tk()
    root.withdraw()

    image_dir = filedialog.askdirectory(title="Select a directory")

    if not image_dir:
        messagebox.showinfo("Cancelled", "No directory was selected.")
        root.destroy()
        return

    img_exist = ds.move_dir_chk_img(image_dir)

    if not img_exist:
        messagebox.showinfo("No Images", "No image files were found in the selected directory.")
        root.destroy()
        return

    imgp.image_process(root, img_exist)

    try:
        root.mainloop()
    finally:
        try:
            root.destroy()
        except Exception:
            pass


if __name__ == "__main__":
    freeze_support()
    main()