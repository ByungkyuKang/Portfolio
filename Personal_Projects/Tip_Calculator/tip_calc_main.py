import flet as ft
import math
import random
import os


def main(page: ft.Page):
    page.title = "Tip Calculator"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 20
    page.scroll = ft.ScrollMode.AUTO

    current_count = [1]

    tip_input_field = ft.TextField(
        hint_text="0.00",
        expand=4,
        border_radius=8,
        on_change=lambda _: calculate_tips(),
        on_blur=lambda e: format_total_tip(e),
    )

    people_input_field = ft.TextField(
        value="1",
        expand=4,
        border_radius=8,
        on_submit=lambda e: handle_people_submit(e),
        on_blur=lambda e: handle_people_submit(e),
    )

    hour_rate_value = ft.Text(
        "0.00",
        expand=3,
        weight=ft.FontWeight.BOLD,
        size=18,
        text_align=ft.TextAlign.RIGHT,
    )

    hour_rate_row = ft.Row(
        controls=[
            ft.Text("Hour Rate", expand=7, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.RIGHT),
            hour_rate_value,
        ],
        spacing=10,
    )

    header = ft.Row(
        controls=[
            ft.Text("Name", expand=6, weight=ft.FontWeight.BOLD),
            ft.Text("Hours", expand=4, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
            ft.Text("Tips", expand=3, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.RIGHT),
        ],
        spacing=10,
    )

    people_list = ft.Column(spacing=10)

    def format_total_tip(e):
        try:
            val = float(e.control.value) if e.control.value else 0.0
            e.control.value = f"{val:.2f}"
            page.update()
        except ValueError:
            e.control.value = ""
            page.update()

    def calculate_tips():
        try:
            raw_tip = float(tip_input_field.value) if tip_input_field.value else 0.0
            total_tip_int = int(round(raw_tip))
        except ValueError:
            raw_tip = 0.0
            total_tip_int = 0

        total_hours = 0.0
        rows_data = []

        for row in people_list.controls:
            h_val = row.controls[1].value
            try:
                h = float(h_val) if h_val else 1.0
                if h < 1.0:
                    h = 1.0
            except ValueError:
                h = 1.0

            total_hours += h
            rows_data.append(h)

        if total_hours > 0:
            rate = raw_tip / total_hours
            hour_rate_value.value = f"{rate:.2f}"

            assigned_tips = []
            remainders = []

            for h in rows_data:
                exact_amount = h * rate
                floor_amount = math.floor(exact_amount)
                assigned_tips.append(floor_amount)
                remainders.append(exact_amount - floor_amount)

            diff = total_tip_int - sum(assigned_tips)

            indexed_remainders = sorted(
                range(len(remainders)),
                key=lambda k: (remainders[k], random.random()),
                reverse=True,
            )

            for i in range(int(diff)):
                idx = indexed_remainders[i % len(indexed_remainders)]
                assigned_tips[idx] += 1

            for i, row in enumerate(people_list.controls):
                row.controls[2].value = f"$ {assigned_tips[i]}"
        else:
            hour_rate_value.value = "0.00"
            for row in people_list.controls:
                row.controls[2].value = "$ 0"

        page.update()

    def on_hour_blur(e):
        try:
            val = float(e.control.value) if e.control.value else 1.0
            if val < 1.0:
                val = 1.0
            e.control.value = f"{val:.2f}"
            page.update()
            calculate_tips()
        except ValueError:
            e.control.value = ""
            page.update()
            calculate_tips()

    def create_person_row():
        return ft.Row(
            controls=[
                ft.TextField(hint_text="Name", expand=6, border_radius=8),
                ft.TextField(
                    hint_text="1.00",
                    expand=4,
                    border_radius=8,
                    text_align=ft.TextAlign.CENTER,
                    on_change=lambda _: calculate_tips(),
                    on_blur=on_hour_blur,
                ),
                ft.Text(
                    "$ 0",
                    expand=3,
                    size=18,
                    weight=ft.FontWeight.BOLD,
                    text_align=ft.TextAlign.RIGHT,
                ),
            ],
            spacing=10,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        )

    def handle_people_submit(e):
        val = people_input_field.value.strip()
        if not val:
            return

        try:
            new_count = int(val)
            if new_count < 1:
                people_input_field.value = str(current_count[0])
                page.update()
                return

            old_count = current_count[0]

            if new_count > old_count:
                for _ in range(new_count - old_count):
                    people_list.controls.append(create_person_row())
            elif new_count < old_count:
                for _ in range(old_count - new_count):
                    if people_list.controls:
                        people_list.controls.pop()

            current_count[0] = new_count
            calculate_tips()
        except ValueError:
            people_input_field.value = str(current_count[0])
            page.update()

    people_list.controls.append(create_person_row())

    page.add(
        ft.Text("Tip Calculator", size=32, weight=ft.FontWeight.BOLD),
        ft.Divider(),
        ft.Row(
            [
                ft.Text("Total Tips ($):", expand=6, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.RIGHT),
                tip_input_field,
            ]
        ),
        ft.Row(
            [
                ft.Text("Number of People:", expand=6, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.RIGHT),
                people_input_field,
            ]
        ),
        ft.Divider(),
        header,
        people_list,
        ft.Divider(),
        hour_rate_row,
    )


app = ft.run(main, export_asgi_app=True)

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", "8080"))
    uvicorn.run(app, host="0.0.0.0", port=port)