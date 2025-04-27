import streamlit as st
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))
def home_page():
    st.title("Welcome to Nkaran - Diakhangakan")
    # inserting a welcome image
    st.image("../assets/nkaran.png", caption="", use_column_width=False, width=200)
    st.write("This is the home page of the Nkaran application.")
    st.write("Here you can find information about the app and its features.")
    st.write("Use the sidebar to navigate to different sections of the app.")
    st.write("If you have any questions or need help, feel free to check the Help section.")
    st.write("You can also learn more about the app in the About section.")
    st.write("For any inquiries, visit the Contact section.")
    st.write("Enjoy using Nkaran - Diakhangakan!")