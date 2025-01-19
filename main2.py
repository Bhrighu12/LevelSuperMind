import streamlit as st
import json
import requests
import matplotlib.pyplot as plt
from typing import Optional

# Langflow Configurations
BASE_API_URL = "https://api.langflow.astra.datastax.com"
LANGFLOW_ID = "1b4f0b9e-bda0-4cca-ac80-40d6607cf491"
FLOW_ID = "2450fc60-36b8-4898-bbc4-be3d455df407"
APPLICATION_TOKEN = st.secrets["api_keys"]["langflow2_token"]
ENDPOINT = FLOW_ID

# Function to run Langflow
def run_flow(message: str) -> dict:
    api_url = f"{BASE_API_URL}/lf/{LANGFLOW_ID}/api/v1/run/{ENDPOINT}"
    payload = {
        "input_value": message,
        "output_type": "chat",
        "input_type": "chat",
    }
    headers = {"Authorization": "Bearer " + APPLICATION_TOKEN, "Content-Type": "application/json"}
    
    response = requests.post(api_url, json=payload, headers=headers)
    return response.json()

# Streamlit UI - Custom Styling
st.markdown(
    """
    <style>
    .stApp {
        background-color: #1e1e1e;
        color: #ffffff;
    }
    .stTitle, .stMarkdown h1, .stMarkdown h2 {
        color: #FFA500;
        text-align: center;
    }
    .stButton>button {
        background-color: #007BFF;
        color: white;
        font-size: 16px;
        border-radius: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

def main():
    st.title("SoulBuddy - AI-Powered Spiritual Guide")
    # User Input
    message2 = st.text_area("", placeholder="Enter the Name and DOB")
    message3 = st.text_area("", placeholder="Enter the Time and Birthplace")
    message = "The Name and DOB is "+message2+"Time and Birthplace is "+message3

    # Generate Response Button
    if st.button("🚀Let's get your Kundli"):
        if not message:
            st.error("⚠️ Please Enter Details.")
            return

        # Run the flow
        try:
            with st.spinner("✨ Getting  your Kundli..."):
                response = run_flow(message)
                
                if "outputs" in response:
                    output_text = response["outputs"][0]["outputs"][0]["results"]["message"]["text"]
                    st.success("✅ Kundli Generated Successfully!")
                    st.markdown(f"<p>{output_text}</p>", unsafe_allow_html=True)
                    
                else:
                    st.error("❌ No 'outputs' found in the response. Please check the API or input.")

        except Exception as e:
            st.error(f"❌ Error: {str(e)}")
if __name__ == "__main__":
    main()
