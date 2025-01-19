import streamlit as st
import json
import requests
import matplotlib.pyplot as plt
from typing import Optional

# Langflow Configurations
BASE_API_URL = "https://api.langflow.astra.datastax.com"
LANGFLOW_ID = "1dc1ae5a-c517-4716-b853-2a6fb964d6e0"
FLOW_ID = "7d8421aa-0805-4316-9578-bac7c4f4b4c9"
APPLICATION_TOKEN = st.secrets["api_keys"]["langflow_token"]
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
    st.title("Automated Research and Trigger Finder (ART Finder)")
    # User Input
    message2 = st.text_area("", placeholder="Enter the Topic")
    message3 = st.text_area("", placeholder="Enter Brand Guidelines")
    message = "The Topic for Advertisement creation is "+message2+"and brand guidelines are "+message3

    # Generate Response Button
    if st.button("🚀Let's Create you an Advertisement"):
        if not message:
            st.error("⚠️ Please Enter Topic.")
            return

        # Run the flow
        try:
            with st.spinner("✨ Creating your Advertisement..."):
                response = run_flow(message)
                
                if "outputs" in response:
                    output_text = response["outputs"][0]["outputs"][0]["results"]["message"]["text"]
                    st.success("✅ Insights Generated Successfully!")
                    st.markdown(f"<p>{output_text}</p>", unsafe_allow_html=True)
                    
                else:
                    st.error("❌ No 'outputs' found in the response. Please check the API or input.")

        except Exception as e:
            st.error(f"❌ Error: {str(e)}")
if __name__ == "__main__":
    main()
