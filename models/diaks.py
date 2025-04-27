# Use my csv file as a simple dictionary
import pandas as pd
import os
from gtts import gTTS
import sys
from transformers import pipeline


# Use a pre-trained translation model from Hugging Face
pipe = pipeline("translation", model="google-t5/t5-base")


# Load the CSV file
csv_file_path = "../database/diakhanke_dataset.csv"
df = pd.read_csv(csv_file_path)

def translate_with_model(text, src_lang, target_lang):
    """
    Translate text from one language to another using a pre-trained model.
    Args:
        text (str): The text to translate.
        src_lang (str): The source language.
        target_lang (str): The target language.
    Returns:
        str: The translated text.
    """
    # Define the task based on the source and target languages
    task = f"translate {src_lang} to {target_lang}: {text}"
    result = pipe(task)
    return result[0]['translation_text']

def translate_to_diakhanke(text):
    """Search for translation in the DataFrame"""
    text_clean = text.strip().lower()  # Normalize input
    matching_row = df[df['francais'].str.lower() == text_clean]
    return matching_row['diakhanke'].iloc[0] if not matching_row.empty else "Traduction Diakhanké non disponible (bientôt !)"

def speak(text):
    """Convert text to speech"""
    try:
        tts = gTTS(text, lang='fr')
        tts.save("pronunciation.mp3")
        os.system("mpg321 pronunciation.mp3")
        return "pronunciation.mp3"
    except Exception as e:
        print(f"Error in text-to-speech conversion: {e}")
        return None

def add_new_word(francais, anglais, diakhanke):
    """Add a new word to the dictionary"""
    global df
    new_entry = pd.DataFrame({
        'francais': [francais],
        'anglais': [anglais],
        'diakhanke': [diakhanke]
    })
    df = pd.concat([df, new_entry], ignore_index=True)
    df.to_csv(csv_file_path, index=False)