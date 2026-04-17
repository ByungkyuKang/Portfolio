import streamlit as st

st.set_page_config(page_title="Tip Calculator", layout="wide")


# ----------------------------
# Helpers
# ----------------------------
def parse_non_negative_float(value):
    if value is None:
        return 0.0

    s = str(value).strip().replace(",", "")
    if s == "":
        return 0.0

    try:
        num = float(s)
        return num if num >= 0 else 0.0
    except ValueError:
        return 0.0


def is_valid_non_negative_float(value):
    if value is None:
        return True

    s = str(value).strip().replace(",", "")
    if s == "":
        return True

    try:
        return float(s) >= 0
    except ValueError:
        return False


# ----------------------------
# Scoped CSS
# only for people row section
# ----------------------------
st.markdown("""
<style>
/* 사람 row 영역에만 적용 */
.st-key-people_rows div[data-testid="stHorizontalBlock"] {
    flex-wrap: nowrap !important;
    gap: 0.22rem !important;
    align-items: stretch !important;
}

.st-key-people_rows div[data-testid="column"] {
    min-width: 0 !important;
    padding: 0 !important;
}

.st-key-people_rows div[data-testid="column"] > div {
    min-width: 0 !important;
}

.st-key-people_rows div[data-testid="stTextInput"] {
    width: 100% !important;
    margin-bottom: 0 !important;
}

.st-key-people_rows div[data-testid="stTextInput"] > div {
    width: 100% !important;
    min-width: 0 !important;
}

.st-key-people_rows div[data-baseweb="base-input"],
.st-key-people_rows div[data-baseweb="input"] {
    width: 100% !important;
    min-width: 0 !important;
}

.st-key-people_rows div[data-baseweb="base-input"] > div,
.st-key-people_rows div[data-baseweb="input"] > div {
    min-height: 40px !important;
    height: 40px !important;
    padding-left: 0 !important;
    padding-right: 0 !important;
}

.st-key-people_rows input {
    min-width: 0 !important;
    height: 40px !important;
    font-size: 14px !important;
    padding: 0 10px !important;
    line-height: 1.2 !important;
}

.st-key-people_rows .people-header {
    font-weight: 700;
    margin-bottom: 0.28rem;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
    font-size: 14px;
}

.st-key-people_rows .short-label {
    display: none;
}

.st-key-people_rows .people-tip-box {
    width: 100%;
    height: 40px;
    box-sizing: border-box;
    display: flex;
    align-items: center;
    padding: 0 10px;
    border-radius: 8px;
    border: 1px solid rgba(128, 128, 128, 0.20);
    background-color: rgba(128, 128, 128, 0.10);
    color: var(--text-color);
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
    font-size: 14px;
    line-height: 1.2;
}

/* 중간 크기 */
@media (max-width: 700px) {
    .st-key-people_rows div[data-testid="stHorizontalBlock"] {
        gap: 0.14rem !important;
    }

    .st-key-people_rows div[data-baseweb="base-input"] > div,
    .st-key-people_rows div[data-baseweb="input"] > div,
    .st-key-people_rows input,
    .st-key-people_rows .people-tip-box {
        height: 38px !important;
        min-height: 38px !important;
    }

    .st-key-people_rows input,
    .st-key-people_rows .people-tip-box {
        font-size: 13px !important;
        padding-left: 8px !important;
        padding-right: 8px !important;
    }

    .st-key-people_rows .people-header {
        font-size: 13px !important;
    }
}

/* 작은 화면 */
@media (max-width: 520px) {
    .st-key-people_rows div[data-testid="stHorizontalBlock"] {
        gap: 0.08rem !important;
    }

    .st-key-people_rows .full-label {
        display: none !important;
    }

    .st-key-people_rows .short-label {
        display: inline !important;
    }

    .st-key-people_rows div[data-baseweb="base-input"] > div,
    .st-key-people_rows div[data-baseweb="input"] > div,
    .st-key-people_rows input,
    .st-key-people_rows .people-tip-box {
        height: 36px !important;
        min-height: 36px !important;
    }

    .st-key-people_rows input,
    .st-key-people_rows .people-tip-box {
        font-size: 12px !important;
        padding-left: 7px !important;
        padding-right: 7px !important;
    }

    .st-key-people_rows .people-header {
        font-size: 12px !important;
        margin-bottom: 0.18rem !important;
    }
}

/* 아주 작은 화면 */
@media (max-width: 400px) {
    .st-key-people_rows div[data-testid="stHorizontalBlock"] {
        gap: 0.04rem !important;
    }

    .st-key-people_rows div[data-baseweb="base-input"] > div,
    .st-key-people_rows div[data-baseweb="input"] > div,
    .st-key-people_rows input,
    .st-key-people_rows .people-tip-box {
        height: 34px !important;
        min-height: 34px !important;
    }

    .st-key-people_rows input,
    .st-key-people_rows .people-tip-box {
        font-size: 11px !important;
        padding-left: 6px !important;
        padding-right: 6px !important;
    }

    .st-key-people_rows .people-header {
        font-size: 11px !important;
    }
}
</style>
""", unsafe_allow_html=True)


# ----------------------------
# Title
# ----------------------------
st.title("Tip Calculator")
st.divider()


# ----------------------------
# Top inputs
# keep original Streamlit style
# ----------------------------
st.write("Total Tips ($)")
total_tips = st.number_input(
    "Total Tips ($)",
    min_value=0.0,
    step=0.01,
    value=0.0,
    format="%.2f",
    label_visibility="collapsed",
)

st.write("Number of People")
num_of_people = st.number_input(
    "Number of People",
    min_value=1,
    step=1,
    value=1,
    label_visibility="collapsed",
)

st.divider()


# ----------------------------
# STEP 1: Gather hours
# ----------------------------
current_hours = []
invalid_rows = []

for i in range(num_of_people):
    raw_hour = st.session_state.get(f"hour_{i}", "")
    if not is_valid_non_negative_float(raw_hour):
        invalid_rows.append(i + 1)

    current_hours.append(parse_non_negative_float(raw_hour))


# ----------------------------
# STEP 2: Calculate
# ----------------------------
safe_total_tips = total_tips if total_tips is not None else 0.0
total_hours_sum = sum(current_hours)

total_cents = int(round(safe_total_tips * 100))
assigned_cents = [0] * num_of_people

if total_hours_sum > 0:
    raw_cents = [total_cents * (h / total_hours_sum) for h in current_hours]
    assigned_cents = [int(x) for x in raw_cents]

    remaining_cents = total_cents - sum(assigned_cents)

    fractional_parts = [
        (idx, raw_cents[idx] - assigned_cents[idx])
        for idx in range(num_of_people)
    ]
    fractional_parts.sort(key=lambda x: x[1], reverse=True)

    for i in range(remaining_cents):
        idx = fractional_parts[i][0]
        assigned_cents[idx] += 1

assigned_tips = [c / 100 for c in assigned_cents]


# ----------------------------
# People rows section
# only this area is tightly styled
# ----------------------------
people_section = st.container(key="people_rows")

with people_section:
    h1, h2, h3 = st.columns([1.12, 0.72, 0.64], gap="small")

    with h1:
        st.markdown(
            '<div class="people-header"><span class="full-label">Name</span><span class="short-label">N</span></div>',
            unsafe_allow_html=True,
        )

    with h2:
        st.markdown(
            '<div class="people-header"><span class="full-label">Hours</span><span class="short-label">H</span></div>',
            unsafe_allow_html=True,
        )

    with h3:
        st.markdown(
            '<div class="people-header"><span class="full-label">Tips</span><span class="short-label">$</span></div>',
            unsafe_allow_html=True,
        )

    for i in range(num_of_people):
        c1, c2, c3 = st.columns([1.12, 0.72, 0.64], gap="small")

        with c1:
            st.text_input(
                f"Name {i+1}",
                key=f"name_{i}",
                placeholder="Name",
                label_visibility="collapsed",
            )

        with c2:
            st.text_input(
                f"Hours {i+1}",
                key=f"hour_{i}",
                placeholder="0.00",
                label_visibility="collapsed",
            )

        with c3:
            st.markdown(
                f'<div class="people-tip-box">${assigned_tips[i]:,.2f}</div>',
                unsafe_allow_html=True,
            )

    if invalid_rows:
        st.caption(
            f"Rows {', '.join(map(str, invalid_rows))} have invalid Hours values, so they are treated as 0."
        )


st.divider()


# ----------------------------
# Hour Rate
# ----------------------------
st.write("Hour Rate")
if total_hours_sum > 0:
    tip_per_hour = safe_total_tips / total_hours_sum
    st.number_input(
        "Hour Rate",
        min_value=0.0,
        disabled=True,
        value=float(tip_per_hour),
        format="%.2f",
        label_visibility="collapsed",
    )
else:
    st.text_input(
        "Hour Rate",
        disabled=True,
        value="N/A",
        label_visibility="collapsed",
    )