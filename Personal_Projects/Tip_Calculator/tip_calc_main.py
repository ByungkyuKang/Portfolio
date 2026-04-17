import flet as ft
import flet_fastapi
import math
import random
import os

def main(page: ft.Page):
    page.title = "Tip Calculator"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 20

    current_count = [1]

    # --- [위젯 정의] ---
    # 1. 상단 입력부 (Total Tip)
    tip_input_field = ft.TextField(
        hint_text="0.00", 
        expand=2, 
        border_radius=8, 
        on_change=lambda _: calculate_tips(),
        on_blur=lambda e: format_total_tip(e)
    )
    
    # 2. 인원 수 입력부
    people_input_field = ft.TextField(
        value="1", 
        expand=2, 
        border_radius=8,
        on_submit=lambda e: handle_people_submit(e),
        on_blur=lambda e: handle_people_submit(e)
    )

    # 3. Hour Rate 표시부
    hour_rate_value = ft.Text("0.00", expand=1, weight="bold", size=18, text_align="right", color="blueaccent")
    hour_rate_row = ft.Row(
        controls=[ft.Text("Hour Rate", expand=9, weight="bold", text_align="right"), hour_rate_value], 
        spacing=10
    )

    header = ft.Row(
        controls=[
            ft.Text("Name", expand=6, weight="bold"),
            ft.Text("Hours", expand=4, weight="bold", text_align="center"),
            ft.Text("Tips", expand=3, weight="bold", text_align="right"),
        ],
        spacing=10
    )

    people_list = ft.Column(spacing=10)

    # --- [핵심 함수들] ---

    # Total Tip 포맷팅 (포커스 아웃 시 실행)
    def format_total_tip(e):
        try:
            val = float(e.control.value) if e.control.value else 0.0
            e.control.value = f"{val:.2f}"
            page.update()
        except ValueError:
            e.control.value = ""
            page.update()

    # 팁 계산 알고리즘 (Maximum Remainder Method + Random Tie-break)
    def calculate_tips():
        try:
            raw_tip = float(tip_input_field.value) if tip_input_field.value else 0.0
            # 배분할 총액 (정수)
            total_tip_int = int(round(raw_tip))
        except ValueError:
            total_tip_int = 0

        total_hours = 0.0
        rows_data = []

        # 데이터 수집 및 최소 시간(1.0) 보장
        for row in people_list.controls:
            h_val = row.controls[1].value
            try:
                h = float(h_val) if h_val else 1.0
                if h < 1.0: h = 1.0
            except ValueError:
                h = 1.0
            total_hours += h
            rows_data.append(h)

        if total_hours > 0:
            rate = raw_tip / total_hours
            hour_rate_value.value = f"{rate:.2f}"
            
            # 1차 배분: 정수 부분만 할당 및 잔량 계산
            assigned_tips = []
            remainders = []
            for h in rows_data:
                exact_amount = h * rate
                floor_amount = math.floor(exact_amount)
                assigned_tips.append(floor_amount)
                remainders.append(exact_amount - floor_amount)

            # 남은 오차(차액) 계산
            diff = total_tip_int - sum(assigned_tips)

            # 정렬 기준 설정: 1순위 잔량(Remainder), 2순위 랜덤값 (동점자 처리용)
            # reverse=True를 통해 큰 값부터 나열
            indexed_remainders = sorted(
                range(len(remainders)), 
                key=lambda k: (remainders[k], random.random()), 
                reverse=True
            )

            # 남은 금액을 순서대로 1달러씩 배분
            for i in range(int(diff)):
                idx = indexed_remainders[i % len(indexed_remainders)]
                assigned_tips[idx] += 1
            
            # UI 결과 업데이트 (정수 출력)
            for i, row in enumerate(people_list.controls):
                row.controls[2].value = f"$ {assigned_tips[i]}"
        else:
            hour_rate_value.value = "0.00"
            for row in people_list.controls:
                row.controls[2].value = "$0"
        
        page.update()

    def on_hour_blur(e):
        try:
            val = float(e.control.value) if e.control.value else 1.0
            if val < 1.0: val = 1.0
            e.control.value = f"{val:.2f}"
            page.update()
            calculate_tips()
        except ValueError:
            e.control.value = "" # 잘못된 값 입력 시 비움 (placeholder가 1.00으로 보임)
            page.update()
            calculate_tips()

    # 새로운 행 생성 함수 (Placeholder 적용)
    def create_person_row():
        return ft.Row(
            controls=[
                ft.TextField(hint_text="Name", expand=6, border_radius=8),
                ft.TextField(
                    hint_text="1.00", 
                    expand=4, 
                    border_radius=8,
                    text_align="center",
                    on_change=lambda _: calculate_tips(),
                    on_blur=on_hour_blur     
                ),
                ft.Text("$ 0", expand=3, size=18, weight="bold", color="greenaccent", text_align="right")
            ],
            spacing=10,
            vertical_alignment=ft.CrossAxisAlignment.CENTER
        )

    # 인원 수 변경 핸들러 (기존 데이터 보존 로직)
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
                    if people_list.controls: people_list.controls.pop()

            current_count[0] = new_count
            calculate_tips()
        except ValueError:
            people_input_field.value = str(current_count[0])
            page.update()

    people_input_field.on_submit = handle_people_submit
    people_input_field.on_blur = handle_people_submit

    # 초기 화면 설정 (첫 줄 생성)
    people_list.controls.append(create_person_row())

    # 페이지 레이아웃 빌드
    page.add(
        ft.Text("Tip Calculator", size=32, weight="bold"),
        ft.Divider(),
        ft.Row([ft.Text("Total Tips ($):", expand=8, weight="bold", text_align="right"), tip_input_field]),
        ft.Row([ft.Text("Number of People:", expand=8, weight="bold", text_align="right"), people_input_field]),
        ft.Divider(),
        header,        
        people_list,
        ft.Divider(),
        hour_rate_row
    )

app = flet_fastapi.app(
    main,
    web_renderer=ft.WebRenderer.HTML,
    assets_dir="." 
)

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8080))
    uvicorn.run(app, host="0.0.0.0", port=port)