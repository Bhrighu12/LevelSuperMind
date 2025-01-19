import streamlit as st
import requests
from datetime import datetime


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

# Custom CSS for Styling
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
        color: #ffffff;
        font-family: 'Arial', sans-serif;
    }
    .stTitle, .stMarkdown h1, .stMarkdown h2 {
        color: #FFA500;
        text-align: center;
        margin-top: 20px;
    }
    .stButton>button {
        background: linear-gradient(90deg, #ffa726, #fb8c00);
        color: black;
        font-size: 16px;
        font-weight: bold;
        padding: 10px 20px;
        border-radius: 10px;
        border: none;
        box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.2);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    .stButton>button:hover {
        transform: translateY(-3px);
        box-shadow: 0px 8px 12px rgba(0, 0, 0, 0.3);
    }
    .custom-card {
        background: rgba(255, 255, 255, 0.1);
        border: 1px solid #ffa726;
        border-radius: 10px;
        padding: 20px;
        margin: 10px 0;
        color: #ffffff;
    }
    .footer {
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        text-align: center;
        padding: 10px 0;
        font-size: 14px;
        color: #ffffff;
        background: linear-gradient(90deg, #0f2027, #203a43, #2c5364);
        border-top: 1px solid #ffa500;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Main Function
def main():
    st.title("✨ SoulBuddy - AI-Powered Spiritual Guide ✨")
    st.markdown("<hr>", unsafe_allow_html=True)

    # Form Inputs
    st.subheader("Fill in Your Details")
    st.markdown("Please provide the following details to generate your personalized Kundli.")

    with st.form("user_details_form", clear_on_submit=False):
        # Name Field
        name = st.text_input("Name", placeholder="Enter your full name")
        # Date and Time Fields in Proper Dialog Boxes
        dob = st.date_input("Date of Birth",min_value=datetime(1900,1,1), help="Select your date of birth")
        time_of_birth = st.text_input("Time of Birth",placeholder="Enter time of Birth (HH:MM (AM/PM))")
        
        # Birthplace Field
        birthplace = st.text_input("Birthplace", placeholder="Enter your birthplace")
        
        # Submit Button
        submitted = st.form_submit_button("Submit Details")

        # Process Submitted Data
        if submitted:
            if not name or not birthplace:
                st.error("⚠️ Please complete all fields before submitting.")
            else:
                st.success("Details Submitted Successfully!")
                st.markdown(
                    f"""
                    <div class="custom-card">
                        <b>Name:</b> {name}<br>
                        <b>Date of Birth:</b> {dob}<br>
                        <b>Time of Birth:</b> {time_of_birth}<br>
                        <b>Birthplace:</b> {birthplace}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                # Generate Kundli Button
                if st.form_submit_button("🚀 Generate Kundli"):
                    # Construct the message
                    message = f"Name: {name}, Date of Birth: {dob}, Time of Birth: {time_of_birth}, Birthplace: {birthplace}"

                    try:
                        with st.spinner("✨ Generating your Kundli..."):
                            response = run_flow(message)

                            if "outputs" in response:
                                output_text = response["outputs"][0]["outputs"][0]["results"]["message"]["text"]
                                st.success("✅ Kundli Generated Successfully!")
                                st.subheader("Your Personalized Kundli")
                                st.markdown(
                                    f"<div class='custom-card'>{output_text}</div>",
                                    unsafe_allow_html=True
                                )
                            else:
                                st.error("❌ No 'outputs' found in the response. Please check the API or input.")
                    except Exception as e:
                        st.error(f"❌ Error: {str(e)}")

    # Footer
    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown(
        """
        <div class="footer">
            Built with ❤️ by SoulBuddy using LangFlow, AstraDB, and Streamlit
        </div>
        """,
        unsafe_allow_html=True
    )

# Run the app
if __name__ == "__main__":
    main()
