import streamlit as st
import sys
import os

# Add the parent directory to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# Importing pages
from pages.translator import translate_page
from pages.dictionary import dictionary_page
from pages.about import about_page
from pages.contacts import contact_page
from pages.help import help_page
from pages.home import home_page

# Set page config
st.set_page_config(page_title="Learn Diakhangakan", page_icon="🗣️", layout="wide")

# Add logo to the sidebar
st.sidebar.image("../assets/nkaran.png", caption="Nkaran - Diakhangakan", use_container_width=True)

# Sidebar navigation
with st.sidebar:
    selected = st.radio(
        "Main Menu",
        ["🏠 Home", "🔄 Translator", "📚 Dictionary", "ℹ️ About", "📬 Contact", "💡 Help"]
    )
# Main content based on selection
if selected == "🏠 Home":
    home_page()
elif selected == "🔄 Translator":
    translate_page()
elif selected == "📚 Dictionary":
    dictionary_page()
elif selected == "ℹ️ About":
    about_page()
elif selected == "📬 Contact":
    contact_page()
elif selected == "💡 Help":
    help_page()
