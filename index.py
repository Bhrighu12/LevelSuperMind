import streamlit as st
from streamlit_option_menu import option_menu

# Custom CSS for styling
st.markdown(
    """
    <style>
    .main-heading {
        font-size: 32px;
        font-weight: bold;
        color: #4CAF50;
        text-align: center;
        margin-bottom: 20px;
    }
    .sub-heading {
        font-size: 18px;
        font-weight: 500;
        color: #555;
        text-align: center;
        margin-bottom: 40px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# App Header
st.markdown('<div class="main-heading">Welcome to Your AI Solutions</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-heading">Choose a tool to get started</div>', unsafe_allow_html=True)

# Sidebar navigation with enhanced UI
selected = option_menu(
    "Navigation",
    ["ART Finder", "Soulful Buddy"],
    icons=["search", "heart"],  # Add icons for each option
    menu_icon="cast",  # Main menu icon
    default_index=0,
    orientation="horizontal",
    styles={
        "container": {"padding": "5px", "background-color": "#f9f9f9"},
        "icon": {"color": "#4CAF50", "font-size": "18px"},
        "nav-link": {
            "font-size": "16px",
            "text-align": "center",
            "margin": "0px",
            "--hover-color": "#ddd",
        },
        "nav-link-selected": {"background-color": "#4CAF50", "color": "white"},
    },
)

# Logic to switch between tools
if selected == "ART Finder":
    st.markdown("<h3 style='text-align: center;'>ART Finder</h3>", unsafe_allow_html=True)
    exec(open("main.py", encoding="utf-8").read())
elif selected == "Soulful Buddy":
    st.markdown("<h3 style='text-align: center;'>Soulful Buddy</h3>", unsafe_allow_html=True)
    exec(open("main2.py", encoding="utf-8").read())