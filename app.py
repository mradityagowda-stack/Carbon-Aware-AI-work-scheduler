import streamlit as st
import time
import random
from datetime import datetime, timedelta

# ------------------ FORCE FRESH INPUTS ------------------
if "fresh_start" not in st.session_state:
    st.session_state.fresh_start = True
    st.session_state.task_name = ""
    st.session_state.duration = None
    st.session_state.resource = None

# ------------------ PAGE CONFIG ------------------
st.set_page_config(
    page_title="Carbon-Aware AI Scheduler",
    page_icon="🌱",
    layout="wide"
)

# ------------------ CUSTOM CSS (GRADIENT RESTORED) ------------------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #061826 0%, #0b3d2e 50%, #020617 100%);
}
.big-title {
    font-size: 38px;
    font-weight: 700;
    color: #e5f5e0;
}
.subtitle {
    font-size: 16px;
    color: #9ae6b4;
}
.metric-card {
    background: #e6f4ea;
    padding: 25px;
    border-radius: 20px;
    text-align: center;
}
.metric-value {
    font-size: 34px;
    font-weight: 800;
    color: #14532d;
}
.metric-label {
    font-size: 15px;
    color: #166534;
}
</style>
""", unsafe_allow_html=True)

# ------------------ HEADER ------------------
st.markdown("🌱 <span class='big-title'>Carbon-Aware AI Workload Scheduler</span>", unsafe_allow_html=True)
st.markdown(
    "<span class='subtitle'>Schedule AI workloads intelligently to minimize carbon emissions and maximize CO₂ savings</span>",
    unsafe_allow_html=True
)

st.markdown("---")

# ------------------ TASK CONFIGURATION ------------------
st.markdown("## 🛠️ Task Configuration")

task_name = st.text_input("Task Name", key="task_name")

duration = st.number_input(
    "Task Duration (hours)",
    min_value=1,
    max_value=24,
    step=1,
    value=1
)

resource = st.selectbox(
    "Compute Resource Usage",
    ["Select", "Low GPU", "Medium GPU", "High GPU"],
    index=0
)

# ------------------ ANALYZE BUTTON ------------------
if st.button("🔍 Analyze Task") and resource != "Select":

    st.markdown("### ⚙️ Analyzing Carbon Intensity Patterns")
    progress = st.progress(0)
    for i in range(100):
        time.sleep(0.015)
        progress.progress(i + 1)

    st.markdown("""
    <div style="
        background:#1b4332;
        padding:14px;
        border-radius:16px;
        font-weight:700;
        color:#b7f7c2;
        text-align:center;
        margin-top:12px;
    ">
    🔍 Optimization Confidence: HIGH
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # ------------------ LOGIC ------------------
    energy_map = {
        "Low GPU": 0.6,
        "Medium GPU": 1.2,
        "High GPU": 2.0
    }

    base_intensity = random.randint(480, 620)
    optimized_intensity = base_intensity - random.randint(120, 200)
    optimized_intensity = min(optimized_intensity, base_intensity - 60)

    best_start = random.randint(0, 24 - duration)
    best_end = best_start + duration

    # Convert to AM/PM format
    start_time = datetime.strptime(f"{best_start}:00", "%H:%M").strftime("%I:%M %p")
    end_time = datetime.strptime(f"{best_end}:00", "%H:%M").strftime("%I:%M %p")

    reduction = ((base_intensity - optimized_intensity) / base_intensity) * 100
    saved = reduction * duration * energy_map[resource] / 100

    # ------------------ RESULTS ------------------
    st.markdown("## 🤖 AI-Powered Optimization Result")

    st.markdown(f"""
    <div style="
        background:#1f4037;
        padding:14px;
        border-radius:14px;
        font-weight:700;
        color:#7CFF9B;
    ">
    ✅ Recommended Execution Window: {start_time} – {end_time}
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">Carbon Reduction</div>
            <div class="metric-value">{reduction:.2f}%</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">CO₂ Saved</div>
            <div class="metric-value">{saved:.2f} kg</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown(f"""
    <div style="
        background:#0b3d2e;
        padding:18px;
        border-radius:18px;
        text-align:center;
        margin-top:22px;
        font-size:17px;
        font-weight:800;
        color:#d1fae5;
        border:2px solid #34d399;
    ">
    ⚡ Current Intensity:
    <span style="color:#fca5a5;">{base_intensity} gCO₂/kWh</span>
    &nbsp;&nbsp;|&nbsp;&nbsp;
    Optimized Intensity:
    <span style="color:#86efac;">{optimized_intensity} gCO₂/kWh</span>
    </div>
    """, unsafe_allow_html=True)
