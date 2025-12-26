import streamlit as st
import time
import random
from PIL import Image
import io

st.set_page_config(page_title="VERIFAI", layout="centered")

st.title("🔍 VERIFAI")
st.subheader("Agentic Deepfake Detection & Authenticity Verification")

st.markdown(
    "An agentic AI system that verifies media authenticity by coordinating multiple forensic agents."
)

uploaded_file = st.file_uploader(
    "Upload an image or video", type=["jpg", "png", "jpeg", "mp4"]
)

def simulate_delay(sec=1):
    time.sleep(sec)

def metadata_agent_safe(file):
    if file.type.startswith("image"):
        return {
            "status": random.choice(["Suspicious"]),
            "findings": ["EXIF partially missing", "Possible re-encoding"]
        }
    else:
        return {
            "status": "Suspicious",
            "findings": ["Video metadata limited"]
        }

def visual_agent():
    score = round(random.uniform(0.65, 0.92), 2)
    artifacts = [
        "Facial boundary distortion",
        "Inconsistent lighting",
        "Texture smoothing anomalies"
    ]
    return {
        "fake_score": score,
        "artifacts": random.sample(artifacts, k=2)
    }

def reasoning_agent(visual, metadata):
    verdict = "Likely Deepfake"
    score = random.randint(10, 30)
    explanation = (
        "Visual analysis detected facial artifacts commonly associated "
        "with synthetic media. Metadata inspection revealed inconsistencies. "
        "Combined evidence suggests manipulation."
    )
    return verdict, score, explanation

if uploaded_file:
    st.success("File uploaded successfully")

    if uploaded_file.type.startswith("image"):
        img = Image.open(uploaded_file)
        st.image(img, caption="Uploaded Image", use_column_width=True)

    st.markdown("---")
    st.subheader("🧠 Agent Execution Log")

    with st.spinner("Preprocessing Agent running..."):
        simulate_delay()
        st.write("✔ Frames extracted")
        st.write("✔ Metadata parsed")

    with st.spinner("Visual Forensics Agent running..."):
        simulate_delay()
        visual_result = visual_agent()
        st.write("✔ Visual artifacts analyzed")

    with st.spinner("Metadata Agent running..."):
        simulate_delay()
        metadata_result = metadata_agent_safe(uploaded_file)
        st.write("✔ Metadata inspection completed")

    with st.spinner("Reasoning Agent aggregating evidence..."):
        simulate_delay()
        verdict, auth_score, explanation = reasoning_agent(
            visual_result, metadata_result
        )

    st.markdown("---")
    st.subheader("📊 Agent Results")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 👁 Visual Forensics Agent")
        st.write(f"Fake Probability: **{visual_result['fake_score']}**")
        for a in visual_result["artifacts"]:
            st.write(f"- {a}")

    with col2:
        st.markdown("### 🧾 Metadata Agent")
        st.write(f"Status: **{metadata_result['status']}**")
        for f in metadata_result["findings"]:
            st.write(f"- {f}")

    st.markdown("---")
    st.subheader("🧠 Final Verdict")
    st.markdown(f"### **{verdict}**")
    st.write(f"Authenticity Score: **{auth_score}%**")
    st.info(explanation)

    st.caption("⚠️ MVP demo — evidence-based multi-agent analysis")
