import streamlit as st

# Title
st.title('Tip Calculator')

st.divider()
#st.write('- It will round')

# Enter total amount of tips
st.write("Total Tips ($)")
total_tips = st.number_input("Total tips ($)", min_value=0.0, step=.01, value=None, placeholder="0.00", label_visibility="collapsed")
st.write("Number of People")
num_of_people = st.number_input("Number of People", min_value=1, step=1, label_visibility="collapsed")

st.divider()

# Adding people and information
if 'people' not in st.session_state:
    st.session_state['people'] = [{"name": "", "hours": 0.0}]

title_col1, title_col2, title_col3 = st.columns([2,1,1])
with title_col1:
    st.write('Names')
with title_col2:
    st.write('Hours')
with title_col3:
    st.write("Tips")

total_hours = []
cont_col1, cont_col2, cont_col3 = st.columns([2,1,1])
for order in range(num_of_people):
    with cont_col1:
        name = st.text_input(f"Enter name for {order+1} here.", label_visibility="collapsed", placeholder=f"Name")
    with cont_col2:
        hour = st.number_input(f"Enter hours for {order+1} here.", label_visibility="collapsed", min_value=1.00, step=0.01, format="%.2f")
        total_hours.append(hour)

# for order in range(num_of_people):
for i, person_hour in enumerate(total_hours):
    with cont_col3:
        # 1. 팁 계산 (0으로 나누기 방지)
        if sum(total_hours) > 0:
            tip_to_take = round(total_tips * (person_hour / sum(total_hours)))
        else:
            tip_to_take = 0.0

        # 2. HTML로 입력창과 똑같은 디자인의 박스 생성
        # var(--text-color)를 쓰면 브라우저 테마 색상을 그대로 가져옵니다.
        # rgba(128, 128, 128, 0.1)는 살짝 회색빛이 도는 투명 배경입니다.
        st.markdown(f"""
            <div style="
                background-color: rgba(128, 128, 128, 0.1); 
                color: var(--text-color); 
                padding: 5px 12px; 
                border-radius: 8px; 
                border: 1px solid rgba(128, 128, 128, 0.2);
                font-size: 16px;
                height: 40px;
                display: flex;
                align-items: center;
                line-height: 1.5;
                margin-bottom: 16px;
                ">
                {tip_to_take}
            </div>
        """, unsafe_allow_html=True)

st.divider()

# st.columns(1)
st.write("Hour rate")
if sum(total_hours) != 0:
    tip_per_hour = round(total_tips/sum(total_hours), 2)
    st.number_input("Hour rate", min_value=0.0, disabled=True, value=float(tip_per_hour), format="%.2f", label_visibility="collapsed")
else:
    st.text_input("Hour rate", disabled=True, value="N/A", label_visibility="collapsed")