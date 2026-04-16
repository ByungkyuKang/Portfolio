import streamlit as st

# Title
st.title('Tip Calculator')

st.divider()

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

safe_total_tips = total_tips if total_tips is not None else 0.0

for i, person_hour in enumerate(total_hours):
    with cont_col3:
        total_hours_sum = sum(total_hours)
        # 0 division is not allowed, and use safe_total_tips
        if total_hours_sum > 0:
            first_round = round(safe_total_tips * (person_hour / total_hours_sum), 2)
            second_round = round(first_round, 1)
            tip_to_take = round(second_round)
        else:
            tip_to_take = 0.0

        # Applying style
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
                {tip_to_take:.0f}
            </div>
        """, unsafe_allow_html=True)

st.divider()

# Hour rate
st.write("Hour rate")
total_hours_sum = sum(total_hours)
if total_hours_sum > 0:
    tip_per_hour = round(safe_total_tips / total_hours_sum, 2)
    st.number_input("Hour rate", min_value=0.0, disabled=True, value=float(tip_per_hour), format="%.2f", label_visibility="collapsed")
else:
    st.text_input("Hour rate", disabled=True, value="N/A", label_visibility="collapsed")