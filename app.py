import streamlit as st

# --- Title ---
st.title("🏊 Swim AI Performance Analyzer")

st.write("Enter your swim data to get feedback and race strategy.")

# --- Inputs ---
fifty = st.number_input("50 Free Time (seconds)", value=27.0)
hundred = st.number_input("100 Free Time (seconds)", value=64.0)
first_50 = st.number_input("First 50 Split", value=30.0)
second_50 = st.number_input("Second 50 Split", value=34.0)
age = st.number_input("Age", value=14)
height = st.number_input("Height (inches)", value=68)

# --- Analyze Button ---
if st.button("Analyze"):

    expected_100 = fifty * 2
    drop_off = hundred - expected_100
    split_diff = second_50 - first_50

    st.subheader("📊 Performance Feedback")

    # MAIN diagnosis
    if drop_off > 8 and split_diff > 5:
        st.write("Severe endurance breakdown and pacing issue")
    elif drop_off > 6:
        st.write("Endurance weakness")
    elif split_diff > 4:
        st.write("Pacing problem")
    elif drop_off < 2 and split_diff < 2:
        st.write("Excellent race execution")
    elif fifty > 28:
        st.write("Lack of sprint speed")
    else:
        st.write("Balanced swimmer with small inefficiencies")

    # Scores
    endurance_score = max(0, 10 - drop_off)
    pacing_score = max(0, 10 - abs(split_diff))

    st.write(f"Endurance Score: {round(endurance_score,1)}/10")
    st.write(f"Pacing Score: {round(pacing_score,1)}/10")

    # Race strategy
    st.subheader("🏁 Race Strategy")

    if drop_off > 6:
        st.write("- Go out controlled—your endurance is the limiter")
    else:
        st.write("- You can push the first 50 aggressively")

    if split_diff > 3:
        st.write("- Focus on holding tempo in the second 50")
    else:
        st.write("- Maintain your pacing strategy")

    if fifty > 28:
        st.write("- Explode off the start and build speed early")
    else:
        st.write("- Stay relaxed early and build into the race")

    st.write("- Kick hard last 25")
    st.write("- Stay mentally locked in")
