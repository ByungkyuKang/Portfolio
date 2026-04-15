import streamlit as st

# Title
st.title('Tip Calculator')

st.divider()
#st.write('- It will round')

# Enter total amount of tips
total_tip = st.number_input("Total tips ($)", min_value=0.0, step=.01)

st.divider()

# st.write(st.session_state)
# Adding people and information
if 'people' not in st.session_state:
    st.session_state['people'] = [{"name": "", "hours": 0.0}]

# def add_person():
#     st.session_state.append({"name":"", "hours":0.0})

# st.write(st.session_state)