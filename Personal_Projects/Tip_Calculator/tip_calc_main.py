import streamlit as st

st.set_page_config(page_title="Tip Calculator", layout="wide")

# ---------------- CSS ----------------
st.markdown("""
<style>
/* 전체 여백 */
.block-container {
    padding-top: 1.8rem;
    padding-bottom: 2rem;
}

/* row용 wrapper 느낌 */
.tip-header {
    font-weight: 700;
    margin-bottom: 0.25rem;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}

.tip-box {
    background-color: rgba(128, 128, 128, 0.10);
    color: var(--text-color);
    padding: 0 10px;
    border-radius: 8px;
    border: 1px solid rgba(128, 128, 128, 0.20);
    font-size: 15px;
    height: 40px;
    display: flex;
    align-items: center;
    white-space: nowrap;
    overflow: hidden;
    box-sizing: border-box;
    width: 100%;
}

/* input 폭 줄어들 수 있게 */
div[data-testid="stTextInput"],
div[data-testid="stNumberInput"] {
    width: 100%;
}

/* input 내부 */
div[data-testid="stTextInput"] input,
div[data-testid="stNumberInput"] input {
    min-width: 0 !important;
}

/* 핵심: Streamlit 컬럼이 모바일에서 세로로 쌓이는 거 방지 */
div[data-testid="stHorizontalBlock"] {
    gap: 0.4rem !important;
    flex-wrap: nowrap !important;
    align-items: stretch !important;
}

/* 각 컬럼이 줄어들 수 있게 */
div[data-testid="column"] {
    min-width: 0 !important;
}

/* 컬럼 안 내용도 줄어들 수 있게 */
div[data-testid="column"] > div {
    min-width: 0 !important;
}

/* 아주 좁은 화면에서 폰트/패딩 축소 */
@media (max-width: 640px) {
    .tip-header {
        font-size: 0.85rem !important;
        margin-bottom: 0.15rem;
    }

    .tip-box {
        font-size: 13px !important;
        height: 36px !important;
        padding: 0 8px !important;
    }

    div[data-testid="stTextInput"] input,
    div[data-testid="stNumberInput"] input {
        font-size: 13px !important;
        padding-left: 0.45rem !important;
        padding-right: 0.45rem !important;
    }
}
</style>
""", unsafe_allow_html=True)

# ---------------- Title ----------------
st.title("Tip Calculator")
st.divider()

# ---------------- Total Tips ----------------
st.write("Total Tips ($)")
total_tips = st.number_input(
    "Total Tips ($)",
    min_value=0.0,
    step=0.01,
    value=None,
    placeholder="0.00",
    label_visibility="collapsed"
)

# ---------------- Number of People ----------------
st.write("Number of People")
num_of_people = st.number_input(
    "Number of People",
    min_value=1,
    step=1,
    value=1,
    label_visibility="collapsed"
)

st.divider()

# ---------------- STEP 1: Collect Hours ----------------
current_hours = []
for i in range(num_of_people):
    h = st.session_state.get(f"hour_{i}", None)
    current_hours.append(h if h is not None else 0.0)

# ---------------- STEP 2: Calculation ----------------
safe_total_tips = total_tips if total_tips is not None else 0.0
total_hours_sum = sum(current_hours)

# 센트 단위 계산
total_cents = int(round(safe_total_tips * 100))
assigned_cents = [0] * num_of_people

if total_hours_sum > 0:
    raw_cents = [total_cents * (h / total_hours_sum) for h in current_hours]
    assigned_cents = [int(x) for x in raw_cents]

    remaining_cents = total_cents - sum(assigned_cents)

    fractional_parts = [(i, raw_cents[i] - assigned_cents[i]) for i in range(num_of_people)]
    fractional_parts.sort(key=lambda x: x[1], reverse=True)

    for i in range(remaining_cents):
        idx = fractional_parts[i][0]
        assigned_cents[idx] += 1

assigned_tips = [c / 100 for c in assigned_cents]

# ---------------- Header Row ----------------
h1, h2, h3 = st.columns([2.2, 1.2, 1.2], gap="small")
with h1:
    st.markdown('<div class="tip-header">Name</div>', unsafe_allow_html=True)
with h2:
    st.markdown('<div class="tip-header">Hours</div>', unsafe_allow_html=True)
with h3:
    st.markdown('<div class="tip-header">Tips</div>', unsafe_allow_html=True)

# ---------------- Data Rows ----------------
for i in range(num_of_people):
    c1, c2, c3 = st.columns([2.2, 1.2, 1.2], gap="small")

    with c1:
        st.text_input(
            f"Name {i+1}",
            key=f"name_{i}",
            label_visibility="collapsed",
            placeholder="Name"
        )

    with c2:
        st.number_input(
            f"Hours {i+1}",
            min_value=0.0,
            step=0.01,
            format="%.2f",
            value=None,
            key=f"hour_{i}",
            label_visibility="collapsed",
            placeholder="Hours"
        )

    with c3:
        st.markdown(
            f'<div class="tip-box">$ {assigned_tips[i]:,.2f}</div>',
            unsafe_allow_html=True
        )

st.divider()

# ---------------- Hour Rate ----------------
st.write("Hour Rate")

if total_hours_sum > 0:
    tip_per_hour = safe_total_tips / total_hours_sum
    st.number_input(
        "Hour Rate",
        min_value=0.0,
        disabled=True,
        value=float(tip_per_hour),
        format="%.2f",
        label_visibility="collapsed"
    )
else:
    st.text_input(
        "Hour Rate",
        value="N/A",
        disabled=True,
        label_visibility="collapsed"
    )