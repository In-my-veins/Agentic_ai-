import streamlit as st
from dotenv import load_dotenv
from langchain_groq import ChatGroq

# Load environment variables
load_dotenv()

# Configure the LLM
llm = ChatGroq(
    model="openai/gpt-oss-120b"
)

# --------------------------------------------------
# Streamlit UI
# --------------------------------------------------

st.set_page_config(
    page_title="Medical Report Analyzer",
    page_icon="🩺",
    layout="centered"
)

st.title("🩺 Medical Report Analyzer")
st.write(
    "Upload a blood report and the application will extract "
    "the test values and classify them according to the "
    "reference ranges provided in the report."
)

uploaded_file = st.file_uploader(
    "Upload your blood report",
    type=["txt"]
)

# --------------------------------------------------
# Process the uploaded report
# --------------------------------------------------

if uploaded_file is not None:

    blood_work = uploaded_file.read().decode("utf-8")

    st.subheader("📄 Uploaded Report")

    with st.expander("View report"):
        st.text(blood_work)

    if st.button("Analyze Report"):

        extraction_prompt = f"""
You are a medical data extraction assistant.

From the blood report below, extract all test values and classify each
one as HIGH, LOW, or NORMAL based on the reference ranges provided
in the report.

Format your response as:

-Test Name: Value | Status: HIGH/LOW/NORMAL | Reference: range

Do not invent reference ranges that are not present in the report.

Blood Report:
{blood_work}
"""

        with st.spinner("Analyzing blood report..."):

            response = llm.invoke(extraction_prompt)

            extracted_values = response.content

        st.subheader("🧪 Extracted Results")

        st.markdown(extracted_values)

        st.info(
            "This application provides general informational analysis "
            "and is not a medical diagnosis. Abnormal results should "
            "be discussed with a qualified healthcare professional."
        )