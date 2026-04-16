import streamlit as st

# Title
st.title('Tip Calculator')

st.divider()

# Get total tips
st.write("Total Tips ($)")
total_tips = st.number_input(
    "Total tips ($)",
    min_value=0.0, 
    step=.01, 
    value=None, 
    placeholder="0.00", 
    label_visibility="collapsed"
)

# Get total number of people
st.write("Number of People")
num_of_people = st.number_input(
    "Number of People", 
    min_value=1, 
    step=1, 
    label_visibility="collapsed"
)

st.divider()

# STEP 1: Data collection - Gethering hours
current_hours = []
for i in range(num_of_people):
    # Retrieving hour values using keys
    # Default value is 0.0 if an ID is not found
    h = st.session_state.get(f"hour_{i}", 0.0)
    if h != None:
        current_hours.append(h)
    else:
        current_hours.append(0.00)

# STEP 2: Caculation
safe_total_tips = total_tips if total_tips is not None else 0.0
total_hours_sum = sum(current_hours)
assigned_tips = [0] * num_of_people

# Applying the Maximum Remainder Method to ensure a fair distribution
# of the total tips. This minimizes discrepancies and eliminates any 
# mismatch between the total tip amount and the sum of distributed tips by
# allocating remaining dollars in a way that reduces perceived unfairness
if total_hours_sum > 0:    
    raw_shares = [safe_total_tips * (h / total_hours_sum) for h \
                  in current_hours]
    assigned_tips = [int(s) for s in raw_shares]
    remaining_dollars = int(round(safe_total_tips - sum(assigned_tips)))
    
    fractional_parts = [(i, s - int(s)) for i, s in enumerate(raw_shares)]
    fractional_parts.sort(key=lambda x: x[1], reverse=True)
    
    for i in range(remaining_dollars):
        idx = fractional_parts[i][0]
        assigned_tips[idx] += 1

# STEP 3: Display - Creating the layout using calculated assigned_tips
for order in range(num_of_people):
    with st.container(border=True):
        st.write(f"**Person {order+1}**")

        # Arrange Name, Hours, and Tips horizontally
        c1, c2, c3 = st.columns([1, 1, 1])
        with c1:
            st.write("Name")
            st.text_input(
            f"Enter name for {order+1} here.", 
            label_visibility="collapsed", 
            placeholder="Name", 
            key=f"name_{order}"
        )
        with c2:
            st.write("Hours")
            st.number_input(
                f"Enter hours for {order+1}", 
                label_visibility="collapsed",
                min_value=1.00,
                step=0.01, 
                format="%.2f",
                value=None,
                key=f"hour_{order}"
            )
        with c3:
            st.write("Tips")
            tip_val = assigned_tips[order]
            # CSS Styling the tip result as a custom box
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
                            $ {tip_val:,}
                        </div>
            """, unsafe_allow_html=True)

st.divider()

# Hourly Rate
st.write("Hour Rate")
if total_hours_sum > 0:
    tip_per_hour = round(safe_total_tips / total_hours_sum, 2)
    st.number_input(
        "Hour rate", 
        min_value=0.0, 
        disabled=True, 
        value=float(tip_per_hour), 
        format="%.2f", 
        label_visibility="collapsed"
    )
else:
    st.text_input(
        "Hour rate", 
        disabled=True, 
        value="N/A", 
        label_visibility="collapsed"
    )