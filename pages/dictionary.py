import streamlit as st
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))

from models.diaks import add_new_word

def dictionary_page():
    st.title("Add a new word to the Diakhanke dictionary")

    francais_input = st.text_input("Word/phrase in French")
    anglais_input = st.text_input("Translation in English")
    diakhanke_input = st.text_input("Translation in Diakhanke")

    if st.button("Add to dictionary"):
        if francais_input and anglais_input and diakhanke_input:
            add_new_word(francais_input, anglais_input, diakhanke_input)
            st.success(f"The word '{francais_input}' has been added to the dictionary!")
        else:
            st.warning("Please fill in all fields.")
