# 📸 Helper to Organize Images

## 📌 Overview

A Python-based image organization tool designed to efficiently detect and manage duplicate or visually similar images.

The application groups similar images and provides an interactive UI to:

- View duplicate groups
- Compare images visually
- Select and manage files
- Automatically clean up duplicates

This tool is optimized for large-scale image collections and focuses on both performance and usability.

---

## 🎯 Motivation

Managing photos across multiple devices often leads to:

- Duplicate files
- Slightly modified versions (resized, compressed, brightness-adjusted)
- Disorganized image collections

The original implementation relied on pairwise feature comparisons, which did not scale well.

This project was redesigned to:

- Improve performance and scalability
- Reduce unnecessary comparisons
- Handle thousands of images efficiently
- Provide a user-friendly interface for managing results

---

## ⚙️ How It Works

The system uses a multi-stage pipeline optimized for performance:

### 1. Metadata Preloading
- Load lightweight image metadata once
- Avoid repeated disk I/O

### 2. Exact Match Detection (MD5)
- Quickly identify identical files

### 3. Candidate Filtering (pHash)
- Convert images into perceptual hashes
- Narrow down candidate images based on similarity

### 4. Optional Fine Comparison (ORB)
- Applied only when necessary
- Improves accuracy for near-duplicates

### 5. Grouping (Union-Find)
- Efficiently merge similar images into groups

### 6. Parallel Processing
- Uses multiprocessing for faster comparisons

---

## 🖥️ User Interface Features

After analysis, the application displays an interactive panel:

### 📂 Group Visualization
- Duplicate images are grouped together
- Unique images are hidden by default (can be toggled)
- Images are sorted by resolution (highest → lowest)

### 🖱️ Interaction
- **Single click** → Select image  
- **Double click** → Open full-size preview  

### 🧰 Actions
- **Show / Hide Unique**  
  Toggle visibility of unique images

- **Mark as Unique**  
  Remove selected images from duplicate groups

- **Delete Selected**  
  Delete selected image files

- **Auto Cleanup**  
  Keep the highest-resolution image in each group and remove the rest

### 📄 Pagination (Performance Optimization)
- Displays images in pages to prevent memory overflow
- Avoids `Fail to allocate bitmap` errors in Tkinter
- Ensures smooth performance even with thousands of images

---

## 🧠 Key Design Decisions

- Load image metadata only once
- Avoid O(n²) comparisons
- Use hash-based filtering before expensive operations
- Perform heavy computations only when necessary
- Limit UI rendering to reduce memory usage
- Hide unique images by default to reduce UI complexity
- Use pagination to prevent excessive memory usage

---

## 🚀 Performance Improvements

### Before
- Pairwise comparisons (near O(n²))
- All images rendered at once
- High memory usage
- UI lag with large datasets

### After
- Hash-based candidate reduction
- Selective ORB computation
- Multiprocessing
- Pagination-based UI rendering
- Lazy loading of images

**Result:**
- Significantly faster processing
- Scalable to thousands of images
- Stable memory usage
- Smooth UI interaction

---

## 🗂 File Structure

### `image_process_main.py`
- Entry point of the application
- Opens directory selection dialog
- Initializes Tkinter root
- Starts the processing pipeline

---

### `img_processing.py`
- Main controller of the application
- Handles:
  - Scan mode selection (Fast / Precise)
  - Progress UI
  - Result panel UI
  - User interactions (select, delete, cleanup)
  - Pagination system
  - Unique image toggle

---

### `img_comp.py`
- Core image comparison engine
- Responsibilities:
  - Compute perceptual hashes (pHash)
  - Filter candidate pairs
  - Perform optional ORB comparison
  - Group images using Union-Find
  - Return duplicate and unique groups

---

### `img_directory.py`
- Handles file system operations
- Responsibilities:
  - Validate directory path
  - Collect image files
  - Return list of image paths

---

## 🔧 Future Improvements

- GIF multi-frame hashing support
- Folder-based grouping options
- Advanced similarity threshold tuning
- GPU acceleration for feature extraction
- Drag-and-drop UI support

---

## 💡 Summary

This project demonstrates:

- Efficient algorithm design for large datasets
- Practical use of hashing and grouping techniques
- Performance optimization strategies
- Real-world GUI application development with Tkinter

🌐 GitHub Repository

https://github.com/ByungkyuKang/Personal_Projects/Unique_Img_Process_with_Python
