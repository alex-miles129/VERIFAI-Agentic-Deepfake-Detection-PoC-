# VERIFAI  
### Agentic AI for Deepfake Detection & Authenticity Verification (PoC)

VERIFAI is a proof-of-concept **agentic AI system** designed to verify the authenticity of digital media such as images and videos.  
Instead of relying on a single black-box model, VERIFAI coordinates **multiple independent agents** that analyze different forensic signals and produce an **evidence-based, explainable verdict**.

This project was developed as part of a hackathon under the *Agentic AI* problem statement.

---

## 🚨 Problem Statement
Deepfakes are becoming increasingly realistic and accessible, making it difficult to trust digital media.  
Most existing solutions depend on a single detection model, which:
- Fails under new manipulation techniques
- Provides poor explainability
- Cannot adapt easily to evolving threats

---

## 💡 Solution Overview
VERIFAI introduces an **agentic, multi-modal approach** to deepfake detection.

Each agent specializes in analyzing a different aspect of the media, and a reasoning agent aggregates their findings to generate a transparent verdict.

Instead of asking *“Is this fake?”*, VERIFAI answers:
> **“What evidence suggests this media is manipulated?”**

---

## 🧠 Agent Architecture

**Agents in the MVP:**
- **Visual Forensics Agent**
  - Detects facial boundary distortions
  - Identifies texture smoothing anomalies
  - Outputs a probabilistic manipulation score

- **Metadata Agent**
  - Analyzes EXIF availability
  - Detects possible re-encoding aware patterns
  - Flags suspicious provenance signals

- **Reasoning Agent**
  - Aggregates evidence from all agents
  - Produces a final verdict with explanation
  - Outputs an authenticity confidence score

---

## 🔄 PoC Demo Flow
1. User uploads an image or video
2. Media is preprocessed
3. Independent agents analyze forensic signals
4. Reasoning agent combines evidence
5. System outputs:
   - Authenticity score
   - Agent-wise findings
   - Human-readable explanation

---

## 📊 Sample Output
The system generates structured results such as:
- Fake probability from visual analysis
- Metadata status (clean / suspicious)
- Final verdict (e.g., *Likely Deepfake*)
- Confidence-based authenticity score

This emphasizes **explainability over blind classification**.

---

## 🛠 Tech Stack
- Python
- Streamlit (UI & demo)
- Pillow (image handling)
- Simulated agent logic (MVP)

---

## ⚠️ Important Note
This repository represents a **Proof of Concept (PoC)**.

- Some agent outputs are simulated to demonstrate system flow
- Architecture is designed to plug in production-grade models
- Focus is on **agentic design, reasoning, and explainability**

---

## 🚀 Future Scope
- Audio deepfake detection agent
- Temporal consistency analysis for videos
- Blockchain-based media provenance
- Real-time social media verification

---

## 🏁 Conclusion
VERIFAI demonstrates how an **agentic AI architecture** can improve trust in digital media by combining independent forensic evidence with transparent reasoning.

As synthetic media evolves, **verification must move beyond single-model detection** — toward explainable, modular, and adaptive systems.

---

