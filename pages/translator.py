import streamlit as st
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.diaks import translate_with_model, translate_to_diakhanke, speak

def translate_page():
    st.title("Translator")
    st.write("Translate text to Diakhanke with pronunciation")

    input_text = st.text_area("Enter text in French or English")
    lang_choice = st.radio("Text language:", ("french", "english"))

    if st.button("Translate to Diakhanke"):
        if input_text:
            intermediate_translation = translate_with_model(input_text, lang_choice, "diakhanke")
            final_translation = translate_to_diakhanke(intermediate_translation)

            st.info(f"Intermediate translation: {intermediate_translation}")
            st.success(f"Final translation in Diakhanke: {final_translation}")

            speak(final_translation)
        else:
            st.warning("Please enter some text.")
