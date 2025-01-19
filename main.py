import streamlit as st
import json
import requests
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

# Custom Styling
st.markdown(
    """
    <style>
    /* App Background */
    .stApp {
        background: linear-gradient(135deg, #141e30, #243b55); /* Elegant gradient */
        color: #ffffff;
        font-family: 'Arial', sans-serif;
        transition: background-color 0.3s ease-in-out;
    }
    
    /* Header Title */
    .stTitle, .stMarkdown h1, .stMarkdown h2 {
        color: #FFA500;
        text-align: center;
        margin-top: 20px;
        animation: fadeIn 2s ease-in-out;
    }
    
    /* Buttons */
    .stButton>button {
        background: linear-gradient(90deg, #ff8c00, #ffa500);
        color: white;
        font-size: 16px;
        font-weight: bold;
        padding: 10px 20px;
        border-radius: 8px;
        border: none;
        box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.2);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    .stButton>button:hover {
        transform: translateY(-3px);
        box-shadow: 0px 8px 12px rgba(0, 0, 0, 0.3);
    }
    
    /* Custom Card Styling */
    .custom-card {
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.1), rgba(255, 255, 255, 0.05));
        border: 1px solid #FFA500;
        border-radius: 10px;
        padding: 20px;
        margin: 10px 0;
        color: #ffffff;
        animation: slideIn 1.5s ease-in-out;
    }
    
    /* Custom Input Styling */
    .custom-input {
        background-color: rgba(255, 255, 255, 0.2);
        border: 1px solid #ffa500;
        color: white;
        padding: 10px;
        border-radius: 8px;
    }

    /* Divider Animation */
    hr {
        border: 0;
        height: 2px;
        background-image: linear-gradient(to right, #ffa500, #ff8c00);
        animation: growWidth 1.5s ease-in-out;
    }

    /* Footer */
    .footer {
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        text-align: center;
        padding: 10px 0;
        font-size: 14px;
        color: #ffffff;
        background: linear-gradient(90deg, #141e30, #243b55);
        border-top: 1px solid #FFA500;
    }
    
    /* Animations */
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }
    @keyframes slideIn {
        from { transform: translateY(20px); opacity: 0; }
        to { transform: translateY(0); opacity: 1; }
    }
    @keyframes growWidth {
        from { width: 0; }
        to { width: 100%; }
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Main Function
def main():
    st.title("✨ Automated Research and Trigger Finder (ART Finder) ✨")
    st.markdown("<hr>", unsafe_allow_html=True)

    # Section 1: Inputs with better layout
    st.subheader("Enter Details")
    st.markdown(
        "Fill in the details below to generate insights and advertisements. Provide a topic and brand guidelines."
    )
    col1, col2 = st.columns([1, 1])
    with col1:
        message2 = st.text_area(
            "Topic", 
            placeholder="E.g., Eco-Friendly Products", 
            height=150, 
            key="topic_input"
        )
    with col2:
        message3 = st.text_area(
            "Brand Guidelines", 
            placeholder="E.g., Sustainability-focused messaging", 
            height=150, 
            key="guidelines_input"
        )

    # Combine inputs
    message = f"The Topic for Advertisement creation is {message2} and brand guidelines are {message3}"

    st.markdown("<hr>", unsafe_allow_html=True)

    # Section 2: Generate Results Button
    center_container = st.container()
    with center_container:
        st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
        if st.button("🚀 Generate Insights"):
            if not message2 or not message3:
                st.error("⚠️ Please fill in both fields!")
            else:
                try:
                    with st.spinner("✨ Generating insights..."):
                        response = run_flow(message)

                        if "outputs" in response:
                            output_text = response["outputs"][0]["outputs"][0]["results"]["message"]["text"]

                            # Section 3: Display Results
                            st.success("✅ Insights Generated Successfully!")
                            st.subheader("Generated Insights")
                            st.markdown(
                                f"<div class='custom-card'>{output_text}</div>", 
                                unsafe_allow_html=True
                            )
                        else:
                            st.error("❌ No 'outputs' found in the response. Please check the API or input.")
                except Exception as e:
                    st.error(f"❌ Error: {str(e)}")
        st.markdown("</div>", unsafe_allow_html=True)

    # Footer Section
    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown(
        """
        <div class="footer">
            Built with ❤️ using LangFlow, AstraDB, and Streamlit
        </div>
        """,
        unsafe_allow_html=True
    )

# Run the app
if __name__ == "__main__":
    main()
