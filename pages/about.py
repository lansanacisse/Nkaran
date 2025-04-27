import streamlit as st

def about_page():
    st.title("About Nkaran")
    st.write("Nkaran is a translation and learning application for Diakhanke.")
    st.markdown("""
    ### Features:
    - Sentence translation between French, English and Diakhanke
    - Audio pronunciation of translations
    - Integrated dictionary to learn new words
    """)
    st.markdown("""
    ### Contributors:
    - **tandian**: Data scientist and machine learning engineer
    - **Nkaran Team**: A group of passionate developers and linguists
    - **Diakhanke Community**: For their invaluable support and feedback
    """)
