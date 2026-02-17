📸 Helper to Organize Images

📌 Overview

This is a Python-based image organization tool designed to simplify personal photo management.

It groups visually similar or duplicate images by inserting numbered prefixes at the beginning of filenames, making it 

easier to identify and manage related images.

The system is optimized for scalability and can efficiently process large image collections.

🎯 Motivation

Managing photos from multiple devices and applications often results in scattered duplicates and visually similar images (e.g., resized, compressed, or brightness-adjusted versions).

The original implementation relied on pairwise feature matching, which did not scale well for large image collections.

This project was redesigned to:
    
    - Improve performance and scalability
    - Reduce unnecessary image comparisons
    - Handle large image sets efficiently
    - Group visually similar images more accurately


⚙️ How It Works

Instead of performing O(n²) pairwise ORB comparisons, the optimized system uses:

1. Perceptual Hashing (pHash)
    - Each image is converted into a perceptual hash representation.

2. Bucketing (LSH-like banding)
    - Hashes are split into bands to generate candidate pairs and reduce unnecessary comparisons.

3. Hamming Distance Comparison
    - Only candidate images are compared using hash distance thresholds.

4. Union-Find (Disjoint Set)
    - Efficiently merges similar images into groups.

5. File Renaming
    - Each group receives a unique ID and images are renamed using zero-padded prefixes:
        [001]imageA.jpg
        [001]imageB.jpg
        [002]imageC.jpg

Images that are resized or brightness-adjusted can still be grouped depending on threshold tuning.


🔧 Current Status

Complete and optimized for performance.

Future improvements may include:

    - GIF multi-frame hashing support
    - Optional folder-based grouping
    - GUI progress indicator
    - Advanced similarity threshold tuning


🗂 Files

image_process_main.py

    - Main execution file.
    - Opens a folder selection dialog
    - Collects image filenames
    - Starts the image grouping and renaming pipeline

img_processing.py
    
    - Coordinates the entire workflow.
    - Method: image_process()
        Calls group_similar_images() from img_comp.py to generate similarity groups.
        Assigns group IDs to all images (including standalone images).
        Ensures files skipped during hashing are treated as single-member groups.
        Sorts results and calls name_change() to rename files.

img_comp.py
    
    - Core similarity engine (performance-optimized).
    - Method: group_similar_images()
        Computes perceptual hashes (pHash) once per image.
        Uses band-based bucketing to reduce candidate comparisons.
        Compares candidates using Hamming distance.
        Uses Union-Find (DSU) to merge similar images into groups.
        Returns grouped filename lists.
    - This replaces the original ORB-based pairwise comparison for improved scalability.


img_name_change.py

    - Method: name_change()
        Accepts a sorted list of (filename, group_id) tuples.
        Applies zero-padded group numbering as a prefix.
        Uses a two-pass renaming strategy to prevent filename conflicts.

img_directory.py

    - Method: move_dir_chk_img()
        Validates the input directory.
        Changes the working directory.
        Checks for image file existence.
        Returns the list of image filenames.

🚀 Performance Improvement

The original design relied on repeated pairwise image comparisons (near O(n²) complexity).

The current version reduces unnecessary comparisons through hash indexing and grouping optimization, significantly improving scalability for large datasets.

🌐 GitHub Repository

https://github.com/ByungkyuKang/Personal_Projects/Unique_Img_Process_with_Python
