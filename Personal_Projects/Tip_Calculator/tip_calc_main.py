import streamlit as st

# Title
st.title('Tip Calculator')

st.divider()

# Input: Total amount of tips
st.write("Total Tips ($)")
total_tips = st.number_input(   "Total tips ($)",
                                min_value=0.0, 
                                step=.01, 
                                value=None, 
                                placeholder="0.00", 
                                label_visibility="collapsed"   )

# Input: Number of people to split
st.write("Number of People")
num_of_people = st.number_input(    "Number of People", 
                                    min_value=1, 
                                    step=1, 
                                    label_visibility="collapsed"    )

st.divider()

# Header columns for employee list
title_col1, title_col2, title_col3 = st.columns([2,1,1])
with title_col1:
    st.write('Names')
with title_col2:
    st.write('Hours')
with title_col3:
    st.write("Tips")

# Create input rows for each person
total_hours = []
cont_col1, cont_col2, cont_col3 = st.columns([2,1,1])

for order in range(num_of_people):
    with cont_col1:
        st.text_input(  f"Enter name for {order+1} here.", 
                        label_visibility="collapsed", 
                        placeholder="Name", 
                        key=f"name_{order}"  )
    with cont_col2:
        hour = st.number_input( f"Enter hours for {order+1} here.", 
                                label_visibility="collapsed", 
                                min_value=0.0, 
                                step=0.01, 
                                format="%.2f", 
                                key=f"hour_{order}" )
        total_hours.append(hour)

# Handle None value for initial state
safe_total_tips = total_tips if total_tips is not None else 0.0
total_hours_sum = sum(total_hours)

# Algorithm: Maximum Remainder Method for Fair Distribution
# This ensures the sum of distributed tips exactly matches total_tips.
assigned_tips = [0] * num_of_people

if total_hours_sum > 0:
    # 1. Calculate precise share for each person (with decimals)
    raw_shares = [safe_total_tips * (h / total_hours_sum) for h in total_hours]
    
    # 2. Assign the integer part first (floor value)
    assigned_tips = [int(s) for s in raw_shares]
    
    # 3. Calculate remaining dollars due to rounding
    remaining_dollars = int(round(safe_total_tips - sum(assigned_tips)))
    
    # 4. Sort by decimal part (fractional loss) in descending order
    # People with higher decimals (e.g., .98) get priority for the remaining dollars
    fractional_parts = [(i, s - int(s)) for i, s in enumerate(raw_shares)]
    fractional_parts.sort(key=lambda x: x[1], reverse=True)
    
    # 5. Distribute remaining dollars to those with the highest fractional loss
    for i in range(remaining_dollars):
        idx = fractional_parts[i][0]
        assigned_tips[idx] += 1

# Display calculated tips with Edge browser compatibility (HTML/CSS)
for tip in assigned_tips:
    with cont_col3:
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
                {tip}
            </div>
        """, unsafe_allow_html=True)

st.divider()

# Calculation and display of Hourly Tip Rate
st.write("Hour rate")
if total_hours_sum > 0:
    tip_per_hour = round(safe_total_tips/total_hours_sum, 2)
    st.number_input("Hour rate", 
                    min_value=0.0, 
                    disabled=True, 
                    value=float(tip_per_hour), 
                    format="%.2f", 
                    label_visibility="collapsed"  )
else:
    st.text_input(  "Hour rate", 
                    disabled=True, 
                    value="N/A", 
                    label_visibility="collapsed"  )