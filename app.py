import streamlit as st
from agent import placement_agent
from evaluation import extract_score

st.set_page_config(page_title="Placement AI Assistant", layout="wide")

st.title("🎓 Placement Readiness Dashboard")
st.caption("Domain-Specific GenAI System for Campus Placements")

st.markdown("---")

# =============================
# 📄 RESUME SECTION
# =============================
st.header("📄 Resume")

resume_option = st.radio(
    "Choose Resume Input Method",
    ["Upload Resume (.txt)", "Type Resume Manually"]
)

resume_text = ""

if resume_option == "Upload Resume (.txt)":
    uploaded_file = st.file_uploader("Upload your resume", type=["txt"])
    if uploaded_file is not None:
        resume_text = uploaded_file.read().decode("utf-8")
        st.success("Resume uploaded successfully!")
else:
    resume_text = st.text_area("Paste your resume here", height=200)

st.markdown("---")

# =============================
# 🧾 JOB DESCRIPTION
# =============================
st.header("🧾 Job Description")

jd_text = st.text_area(
    "Paste the job description here",
    height=200
)

st.markdown("---")

# =============================
# 🔍 ANALYZE BUTTON
# =============================
if st.button("Analyze Placement Readiness"):

    if resume_text.strip() == "" or jd_text.strip() == "":
        st.warning("Please provide both resume and job description.")
    else:
        with st.spinner("Analyzing..."):
            result = placement_agent(resume_text, jd_text)

        score = extract_score(result)

        st.markdown("## 📊 Placement Readiness Score")

        if score is not None:
            st.progress(score / 100)
            st.metric("Score", f"{score}/100")
        else:
            st.warning("Score not detected.")

        st.markdown("## 📄 Detailed Resume Analysis")
        st.markdown(result)