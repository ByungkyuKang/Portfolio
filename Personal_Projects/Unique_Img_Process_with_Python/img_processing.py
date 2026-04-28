import os
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk, ImageDraw

import img_comp as imgc


BOX_WIDTH = 90
BOX_HEIGHT = 90
THUMB_SIZE = (80, 70)
PREVIEW_MAX_SIZE = (1000, 800)

# Unique images are hidden by default.
SHOW_SINGLETONS = False

ITEM_OUTER_WIDTH = 106
IMAGES_PER_PAGE = 300


def resolution_score(path, meta):
    w, h = meta[path]["size"]
    return w * h


def sort_group_by_resolution_desc(group_paths, meta):
    return sorted(
        group_paths,
        key=lambda p: (
            -resolution_score(p, meta),
            -meta[p]["size"][0],
            -meta[p]["size"][1],
            meta[p]["filename"].lower(),
        )
    )


def make_thumb_with_border(image_path):
    try:
        pil_img = Image.open(image_path).convert("RGB")
        pil_img.thumbnail(THUMB_SIZE)

        bg = Image.new("RGB", (BOX_WIDTH, BOX_HEIGHT), "white")

        x = (BOX_WIDTH - pil_img.width) // 2
        y = (BOX_HEIGHT - pil_img.height) // 2
        bg.paste(pil_img, (x, y))

        draw = ImageDraw.Draw(bg)
        draw.rectangle(
            [(1, 1), (BOX_WIDTH - 2, BOX_HEIGHT - 2)],
            outline="black",
            width=1
        )
        return bg

    except Exception:
        fallback = Image.new("RGB", (BOX_WIDTH, BOX_HEIGHT), "white")
        draw = ImageDraw.Draw(fallback)
        draw.rectangle(
            [(1, 1), (BOX_WIDTH - 2, BOX_HEIGHT - 2)],
            outline="black",
            width=1
        )
        draw.text((10, BOX_HEIGHT // 2 - 8), "Error", fill="black")
        return fallback


def ask_scan_mode(root):
    answer = messagebox.askyesnocancel(
        "Select Scan Mode",
        "Would you like to perform a precise scan?\n\n"
        "Yes = Precise Scan (slower, more accurate)\n"
        "No = Fast Scan (faster)\n"
        "Cancel = Cancel",
        parent=root
    )

    if answer is None:
        return None

    if answer is True:
        return {
            "label": "Precise",
            "hash_distance_threshold": 6,
            "use_orb_for_near_hash": True,
            "orb_match_threshold": 40,
        }

    return {
        "label": "Fast",
        "hash_distance_threshold": 4,
        "use_orb_for_near_hash": False,
        "orb_match_threshold": 40,
    }


def show_progress_window(root, mode_label):
    progress_win = tk.Toplevel(root)
    progress_win.title("Processing Images")
    progress_win.geometry("460x150")
    progress_win.resizable(False, False)

    progress_win.transient(root)
    progress_win.grab_set()
    progress_win.lift()
    progress_win.attributes("-topmost", True)
    progress_win.after(200, lambda: progress_win.attributes("-topmost", False))
    progress_win.focus_force()

    status_var = tk.StringVar(value=f"Starting... ({mode_label} mode)")
    percent_var = tk.StringVar(value="0%")

    frame = tk.Frame(progress_win, padx=20, pady=20)
    frame.pack(fill="both", expand=True)

    mode_lbl = tk.Label(
        frame,
        text=f"Mode: {mode_label}",
        anchor="w",
        font=("Arial", 10, "bold")
    )
    mode_lbl.pack(fill="x", pady=(0, 8))

    lbl = tk.Label(frame, textvariable=status_var, anchor="w", font=("Arial", 11))
    lbl.pack(fill="x", pady=(0, 12))

    bar = ttk.Progressbar(frame, orient="horizontal", mode="determinate", maximum=100)
    bar.pack(fill="x")

    percent_lbl = tk.Label(frame, textvariable=percent_var, anchor="e", font=("Arial", 10))
    percent_lbl.pack(fill="x", pady=(8, 0))

    progress_win.update_idletasks()

    return progress_win, status_var, percent_var, bar


def update_progress_ui(root, status_var, percent_var, bar, message, current, total):
    total = max(total, 1)
    percent = int((current / total) * 100)

    status_var.set(f"{message} ({current}/{total})")
    percent_var.set(f"{percent}%")
    bar["value"] = percent

    root.update_idletasks()


def open_full_image_preview(parent, image_path, meta):
    preview = tk.Toplevel(parent)
    preview.title(meta[image_path]["filename"])
    preview.geometry("1100x900")

    outer = tk.Frame(preview)
    outer.pack(fill="both", expand=True)

    try:
        pil_img = Image.open(image_path).convert("RGB")
        original_w, original_h = pil_img.size

        display_img = pil_img.copy()
        display_img.thumbnail(PREVIEW_MAX_SIZE)

        photo = ImageTk.PhotoImage(display_img, master=preview)

        info_text = (
            f"{meta[image_path]['filename']}\n"
            f"Resolution: {original_w} x {original_h}\n"
            f"Path: {image_path}"
        )

        info_label = tk.Label(
            outer,
            text=info_text,
            justify="left",
            anchor="w",
            font=("Arial", 10)
        )
        info_label.pack(fill="x", padx=12, pady=(12, 8))

        img_label = tk.Label(outer, image=photo, bd=0)
        img_label.pack(padx=12, pady=(0, 12), expand=True)

        preview.photo_ref = photo

    except Exception as e:
        err_label = tk.Label(
            outer,
            text=f"Failed to open preview.\n\n{e}",
            justify="left",
            font=("Arial", 11)
        )
        err_label.pack(padx=20, pady=20)


def image_process(root, img_list):
    mode = ask_scan_mode(root)

    if mode is None:
        try:
            root.destroy()
        except Exception:
            pass
        return

    progress_win, status_var, percent_var, bar = show_progress_window(root, mode["label"])

    comparator = imgc.ImageComparator(
        img_list=img_list,
        hash_distance_threshold=mode["hash_distance_threshold"],
        use_orb_for_near_hash=mode["use_orb_for_near_hash"],
        orb_match_threshold=mode["orb_match_threshold"],
    )

    def progress_callback(message, current, total):
        update_progress_ui(root, status_var, percent_var, bar, message, current, total)

    try:
        duplicate_groups, singleton_groups, meta = comparator.group_duplicates(
            progress_callback=progress_callback
        )
    finally:
        try:
            progress_win.grab_release()
        except Exception:
            pass
        progress_win.destroy()

    duplicate_groups = [sort_group_by_resolution_desc(g, meta) for g in duplicate_groups]
    singleton_groups = [sort_group_by_resolution_desc(g, meta) for g in singleton_groups]

    show_results_window(root, duplicate_groups, singleton_groups, meta, mode["label"])


def show_results_window(root, duplicate_groups, singleton_groups, meta, mode_label):
    window = tk.Toplevel(root)
    window.title("Duplicate Image Groups")
    window.geometry("1400x800")

    selected_paths = set()
    item_widgets = {}
    photo_refs = []
    current_paths = list(meta.keys())

    current_duplicate_groups = [list(g) for g in duplicate_groups]
    current_singleton_groups = [list(g) for g in singleton_groups]

    # Controls whether unique images are shown in the UI.
    show_unique_state = {"value": SHOW_SINGLETONS}

    page_state = {"page": 0}
    last_items_per_row = {"value": None}
    resize_job = {"id": None}

    outer = tk.Frame(window)
    outer.pack(fill="both", expand=True)

    canvas = tk.Canvas(outer, bg="#f3f3f3")
    scrollbar = ttk.Scrollbar(outer, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)

    scrollbar.pack(side="right", fill="y")
    canvas.pack(side="left", fill="both", expand=True)

    content_frame = tk.Frame(canvas, bg="#f3f3f3")
    canvas_window = canvas.create_window((0, 0), window=content_frame, anchor="nw")

    def close_app():
        try:
            canvas.unbind_all("<MouseWheel>")
        except Exception:
            pass

        try:
            window.destroy()
        except Exception:
            pass

        try:
            root.quit()
        except Exception:
            pass

        try:
            root.destroy()
        except Exception:
            pass

        os._exit(0)

    window.protocol("WM_DELETE_WINDOW", close_app)

    def get_items_per_row():
        width = canvas.winfo_width()
        if width <= 1:
            width = 1200

        usable_width = max(width - 40, ITEM_OUTER_WIDTH)
        count = usable_width // ITEM_OUTER_WIDTH
        return max(1, count)

    def count_total_images():
        total = 0

        for group in current_duplicate_groups:
            total += len(group)

        if show_unique_state["value"]:
            for group in current_singleton_groups:
                total += len(group)

        return total

    def get_total_pages():
        total = count_total_images()
        return max(1, (total + IMAGES_PER_PAGE - 1) // IMAGES_PER_PAGE)

    def get_group_entries_for_current_page():
        start = page_state["page"] * IMAGES_PER_PAGE
        end = start + IMAGES_PER_PAGE

        entries = []
        global_index = 0

        def consume_groups(groups, section_name):
            nonlocal global_index

            for group_no, group in enumerate(groups, start=1):
                group_len = len(group)
                group_start_global = global_index
                group_end_global = global_index + group_len

                # Skip if the current page range does not overlap with this group.
                if group_end_global <= start:
                    global_index += group_len
                    continue

                if group_start_global >= end:
                    break

                local_start = max(0, start - group_start_global)
                local_end = min(group_len, end - group_start_global)

                sliced_paths = group[local_start:local_end]

                if sliced_paths:
                    entries.append({
                        "section": section_name,
                        "group_no": group_no,
                        "paths": sliced_paths,
                        "total_count": group_len,   # Total number of items in the group
                        "start_index": local_start, # Start index of the current slice within the group
                    })

                global_index += group_len

        consume_groups(current_duplicate_groups, "Duplicate")

        if show_unique_state["value"]:
            consume_groups(current_singleton_groups, "Unique")

        return entries

    def refresh_page_buttons():
        total_pages = get_total_pages()
        current_page = page_state["page"] + 1

        page_label.config(text=f"Page {current_page} / {total_pages}")
        prev_btn.config(state="normal" if page_state["page"] > 0 else "disabled")
        next_btn.config(state="normal" if page_state["page"] < total_pages - 1 else "disabled")

    def refresh_item_visual(path):
        if path not in item_widgets:
            return

        outer_frame = item_widgets[path]["outer_frame"]
        selected = path in selected_paths

        if selected:
            outer_frame.config(bg="#2b78ff", highlightbackground="#2b78ff", highlightthickness=2)
        else:
            outer_frame.config(bg="#f3f3f3", highlightbackground="#cfcfcf", highlightthickness=1)

    def toggle_selection(path):
        if path in selected_paths:
            selected_paths.remove(path)
        else:
            selected_paths.add(path)

        refresh_item_visual(path)

    def on_single_click(path):
        toggle_selection(path)

    def on_double_click(path):
        open_full_image_preview(window, path, meta)

    def bind_click_recursive(widget, path):
        widget.bind("<Button-1>", lambda event, p=path: on_single_click(p))
        widget.bind("<Double-Button-1>", lambda event, p=path: on_double_click(p))

    def clear_content():
        for child in content_frame.winfo_children():
            child.destroy()

        item_widgets.clear()
        photo_refs.clear()

    def add_group_to_ui(parent, entry, items_per_row):
        section = entry["section"]
        group_no = entry["group_no"]
        group_paths = entry["paths"]
        total_count = entry["total_count"]
        start_index = entry["start_index"]

        if total_count == len(group_paths):
            title = f"{section} Group {group_no} ({total_count} file(s))"
        else:
            end_index = start_index + len(group_paths)
            title = (
                f"{section} Group {group_no} "
                f"(showing {start_index + 1}-{end_index} of {total_count})"
            )

        group_frame = ttk.LabelFrame(parent, text=title, padding=8)
        group_frame.pack(fill="x", padx=10, pady=10, anchor="nw")

        for idx, path in enumerate(group_paths):
            row = idx // items_per_row
            col = idx % items_per_row

            outer_frame = tk.Frame(
                group_frame,
                bg="#f3f3f3",
                highlightbackground="#cfcfcf",
                highlightthickness=1,
                bd=0
            )
            outer_frame.grid(row=row, column=col, padx=5, pady=5, sticky="nw")

            item_frame = tk.Frame(outer_frame, bg="white")
            item_frame.pack(padx=2, pady=2)

            thumb_img = make_thumb_with_border(path)
            photo = ImageTk.PhotoImage(thumb_img, master=window)
            photo_refs.append(photo)

            img_label = tk.Label(item_frame, image=photo, bd=0, bg="white", cursor="hand2")
            img_label.pack()

            width, height = meta[path]["size"]
            filename = meta[path]["filename"]

            text_label = tk.Label(
                item_frame,
                text=f"{filename}\n{width}x{height}",
                justify="center",
                font=("Arial", 7),
                bg="white",
                cursor="hand2"
            )
            text_label.pack(pady=(3, 0))

            item_widgets[path] = {
                "outer_frame": outer_frame,
                "item_frame": item_frame,
                "img_label": img_label,
                "text_label": text_label,
            }

            bind_click_recursive(outer_frame, path)
            bind_click_recursive(item_frame, path)
            bind_click_recursive(img_label, path)
            bind_click_recursive(text_label, path)

            refresh_item_visual(path)

    def normalize_groups_after_file_changes():
        for group in current_duplicate_groups:
            group[:] = [p for p in group if os.path.exists(p)]

        for group in current_singleton_groups:
            group[:] = [p for p in group if os.path.exists(p)]

        current_duplicate_groups[:] = [g for g in current_duplicate_groups if g]
        current_singleton_groups[:] = [g for g in current_singleton_groups if g]

        new_duplicate_groups = []
        new_unique_groups = [list(g) for g in current_singleton_groups]

        for group in current_duplicate_groups:
            if len(group) > 1:
                new_duplicate_groups.append(group)
            elif len(group) == 1:
                new_unique_groups.append([group[0]])

        current_duplicate_groups[:] = new_duplicate_groups
        current_singleton_groups[:] = new_unique_groups

        total_pages = get_total_pages()
        if page_state["page"] >= total_pages:
            page_state["page"] = max(0, total_pages - 1)

    def rebuild_ui(force=False):
        items_per_row = get_items_per_row()

        if not force and last_items_per_row["value"] == items_per_row:
            return

        last_items_per_row["value"] = items_per_row

        clear_content()
        normalize_groups_after_file_changes()

        for i in range(len(current_duplicate_groups)):
            current_duplicate_groups[i] = sort_group_by_resolution_desc(current_duplicate_groups[i], meta)

        for i in range(len(current_singleton_groups)):
            current_singleton_groups[i] = sort_group_by_resolution_desc(current_singleton_groups[i], meta)

        total_images = count_total_images()
        total_pages = get_total_pages()

        unique_status = "Shown" if show_unique_state["value"] else "Hidden"

        header = tk.Label(
            content_frame,
            text=(
                f"Mode: {mode_label}    "
                f"Duplicate groups: {len(current_duplicate_groups)}    "
                f"Unique groups: {len(current_singleton_groups)} ({unique_status})    "
                f"Images displayed: {total_images}    "
                f"Showing up to {IMAGES_PER_PAGE} images/page"
            ),
            font=("Arial", 12, "bold"),
            bg="#f3f3f3"
        )
        header.pack(anchor="w", padx=12, pady=(12, 4))

        page_header = tk.Label(
            content_frame,
            text=f"Page {page_state['page'] + 1} of {total_pages}",
            font=("Arial", 10),
            bg="#f3f3f3"
        )
        page_header.pack(anchor="w", padx=12, pady=(0, 8))

        entries = get_group_entries_for_current_page()

        if not entries:
            no_data = tk.Label(
                content_frame,
                text="No images to display.",
                font=("Arial", 11),
                bg="#f3f3f3"
            )
            no_data.pack(anchor="w", padx=12, pady=10)
        else:
            for entry in entries:
                add_group_to_ui(content_frame, entry, items_per_row)

        content_frame.update_idletasks()
        canvas.configure(scrollregion=canvas.bbox("all"))
        canvas.yview_moveto(0)

        refresh_page_buttons()

    def move_selected_to_unique():
        if not selected_paths:
            messagebox.showinfo("No Selection", "No images are selected.")
            return

        moved_paths = []
        new_duplicate_groups = []
        new_unique_groups = [list(g) for g in current_singleton_groups]

        for group in current_duplicate_groups:
            selected_in_group = [p for p in group if p in selected_paths]
            remaining_in_group = [p for p in group if p not in selected_paths]

            for path in selected_in_group:
                new_unique_groups.append([path])
                moved_paths.append(path)

            if len(remaining_in_group) > 1:
                new_duplicate_groups.append(remaining_in_group)
            elif len(remaining_in_group) == 1:
                new_unique_groups.append([remaining_in_group[0]])

        if not moved_paths:
            messagebox.showinfo(
                "Mark as Unique",
                "None of the selected images are in a duplicate group."
            )
            return

        current_duplicate_groups[:] = new_duplicate_groups
        current_singleton_groups[:] = new_unique_groups

        for path in moved_paths:
            selected_paths.discard(path)

        messagebox.showinfo(
            "Mark as Unique",
            f"{len(moved_paths)} file(s) moved to Unique Images."
        )

        rebuild_ui(force=True)

    def delete_paths(paths_to_delete):
        deleted_count = 0
        failed = []

        for path in paths_to_delete:
            try:
                if os.path.exists(path):
                    os.remove(path)
                    deleted_count += 1
            except Exception as e:
                failed.append(f"{os.path.basename(path)}: {e}")

        if failed:
            msg = "Some files could not be deleted:\n\n" + "\n".join(failed[:10])
            if len(failed) > 10:
                msg += "\n..."
            messagebox.showwarning("Delete Warning", msg)

        return deleted_count

    def on_delete_selected():
        if not selected_paths:
            messagebox.showinfo("No Selection", "No images are selected.")
            return

        selected_list = sorted(selected_paths)

        confirm = messagebox.askyesno(
            "Delete Selected",
            f"Delete {len(selected_list)} selected file(s)?\n\nThis cannot be undone."
        )
        if not confirm:
            return

        deleted_count = delete_paths(selected_list)
        selected_paths.clear()

        normalize_groups_after_file_changes()

        if not any(os.path.exists(p) for p in current_paths):
            messagebox.showinfo("Done", "No image files remain.")
            close_app()
            return

        messagebox.showinfo("Delete Complete", f"Deleted {deleted_count} file(s).")
        rebuild_ui(force=True)

    def on_auto_cleanup():
        deletions = []

        for group in current_duplicate_groups:
            sorted_group = sort_group_by_resolution_desc(group, meta)
            if len(sorted_group) > 1:
                deletions.extend(sorted_group[1:])

        if not deletions:
            messagebox.showinfo("Auto Cleanup", "There are no duplicate files to clean up.")
            return

        confirm = messagebox.askyesno(
            "Auto Cleanup",
            f"Delete {len(deletions)} duplicate file(s)?\n\n"
            f"For each duplicate group, only the highest-resolution image will be kept.\n\n"
            f"This cannot be undone."
        )
        if not confirm:
            return

        deleted_count = delete_paths(deletions)
        selected_paths.clear()

        normalize_groups_after_file_changes()

        if not any(os.path.exists(p) for p in current_paths):
            messagebox.showinfo("Done", "No image files remain.")
            close_app()
            return

        messagebox.showinfo("Auto Cleanup Complete", f"Deleted {deleted_count} file(s).")
        rebuild_ui(force=True)

    def go_prev_page():
        if page_state["page"] > 0:
            page_state["page"] -= 1
            rebuild_ui(force=True)

    def go_next_page():
        if page_state["page"] < get_total_pages() - 1:
            page_state["page"] += 1
            rebuild_ui(force=True)

    def toggle_unique_images():
        """
        Toggle whether unique images are displayed in the result panel.
        """
        show_unique_state["value"] = not show_unique_state["value"]
        page_state["page"] = 0

        if show_unique_state["value"]:
            unique_btn.config(text="Hide Unique")
        else:
            unique_btn.config(text="Show Unique")

        rebuild_ui(force=True)

    bottom_bar = tk.Frame(window)
    bottom_bar.pack(fill="x", side="bottom", padx=10, pady=8)

    left_info = tk.Label(
        bottom_bar,
        text="Single click: select | Double click: open preview",
        font=("Arial", 9)
    )
    left_info.pack(side="left")

    page_control_frame = tk.Frame(bottom_bar)
    page_control_frame.pack(side="left", padx=(20, 0))

    prev_btn = tk.Button(
        page_control_frame,
        text="Previous",
        width=10,
        command=go_prev_page
    )
    prev_btn.pack(side="left", padx=(0, 6))

    page_label = tk.Label(
        page_control_frame,
        text="Page 1 / 1",
        font=("Arial", 9)
    )
    page_label.pack(side="left", padx=(0, 6))

    next_btn = tk.Button(
        page_control_frame,
        text="Next",
        width=10,
        command=go_next_page
    )
    next_btn.pack(side="left")

    button_frame = tk.Frame(bottom_bar)
    button_frame.pack(side="right")

    unique_btn = tk.Button(
        button_frame,
        text="Show Unique",
        width=12,
        command=toggle_unique_images
    )
    unique_btn.pack(side="left", padx=(0, 6))

    exclude_btn = tk.Button(
        button_frame,
        text="Mark as Unique",
        width=14,
        command=move_selected_to_unique
    )
    exclude_btn.pack(side="left", padx=(0, 6))

    delete_btn = tk.Button(
        button_frame,
        text="Delete Selected",
        width=14,
        command=on_delete_selected
    )
    delete_btn.pack(side="left", padx=(0, 6))

    auto_btn = tk.Button(
        button_frame,
        text="Auto Cleanup",
        width=12,
        command=on_auto_cleanup
    )
    auto_btn.pack(side="left")

    def on_frame_configure(event):
        canvas.configure(scrollregion=canvas.bbox("all"))

    def on_canvas_configure(event):
        canvas.itemconfig(canvas_window, width=event.width)

    def on_window_or_canvas_resize(event=None):
        if resize_job["id"] is not None:
            window.after_cancel(resize_job["id"])

        resize_job["id"] = window.after(150, lambda: rebuild_ui(force=False))

    content_frame.bind("<Configure>", on_frame_configure)
    canvas.bind("<Configure>", on_canvas_configure)
    window.bind("<Configure>", on_window_or_canvas_resize)

    def _on_mousewheel(event):
        canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    canvas.bind_all("<MouseWheel>", _on_mousewheel)

    rebuild_ui(force=True)

    window.photo_refs = photo_refs