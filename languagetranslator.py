# -*- coding: utf-8 -*-
"""Untitled7.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1OQAgOVqQyZsill7npvfhS7z2XsI_PHuJ
"""

import streamlit as st
from googletrans import Translator

# Create a Streamlit app title and set a custom app color
st.set_page_config(
    page_title="Language Translator",
    page_icon="✏️",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.markdown(
    """
    <style>
    .css-1v3fvcr {
        background-color: #FF5733;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Create a text input field for the user to enter text
input_text = st.text_area("Enter text to translate:")

# Create a dropdown menu for selecting the target language
target_language = st.selectbox("Select target language:", ["en", "es", "fr", "de", "ja", "zh"])

# Create a dropdown menu for selecting the source language
source_language = st.selectbox("Select source language:", ["auto", "en", "es", "fr", "de", "ja", "zh"])

# Create a function to translate the text
def translate_text(input_text, source_language, target_language):
    try:
        translator = Translator()
        translated = translator.translate(input_text, src=source_language, dest=target_language)
        return translated.text
    except Exception as e:
        return f"Error: {str(e)}"

# Create a button to trigger the translation
if st.button("Translate"):
    if input_text:
        translated_text = translate_text(input_text, source_language, target_language)
        st.success(f"Translated text ({source_language} to {target_language}):")
        st.write(translated_text)
    else:
        st.warning("Please enter text to translate.")

# Add a footer
st.footer("Powered by Google Translate API")
