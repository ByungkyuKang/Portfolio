import img_processing as imgp
import img_directory as ds
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

image_dir = filedialog.askdirectory(title="Select a directory")

img_exist = ds.move_dir_chk_img(image_dir)
imgp.image_process(img_exist)
