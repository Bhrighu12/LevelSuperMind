import streamlit as st

# Sidebar for navigation
option = st.sidebar.radio("Go to:", ["ART Finder", "Soulful Buddy"])

# Logic to switch between files
if option == "ART Finder":
    exec(open("main.py", encoding="utf-8").read())
elif option == "Soulful Buddy":
    exec(open("main2.py", encoding="utf-8").read())
