# 📚 Nkaran - Learn Diakhanké

Welcome to the **Nkaran** application!  
This project aims to help you learn the Diakhanké (Diakango) language through an interactive app featuring automatic translation, audio pronunciation, and a growing dynamic dictionary.



## 🚀 Features

- Translate between **French ↔ Diakhanké** and **English ↔ Diakhanké**.
- Listen to the pronunciation (Text-to-Speech) of translated words.
- Dynamically add new words to the dictionary directly from the app.
- Uses a translation model based on **T5** (`google-t5/t5-base`).
- Clean and user-friendly interface built with **Streamlit**.



## 🛠️ Installation

1. Clone this repository:

```bash
git clone https://github.com/lansanacisse/Nkaran.git
cd Nkaran
```

2. Install the dependencies:

```bash
pip install -r requirements.txt
```

3. Run the Streamlit application:

```bash
streamlit run app.py
```

---

## 📦 Main Dependencies

- `streamlit`
- `transformers`
- `gtts`
- `pandas`
- `torch`
- `sentencepiece`



## 🎯 Future Goals

- Improve the translation model by training a **custom model** for Diakhanké using personalized prompts.
- Build a smart self-learning system based on new word additions.
- Develop a lightweight mobile app (Android/iOS) using Flutter or Streamlit Mobile.
- Enable offline mode for translation and pronunciation.


## 📄 License

This project is licensed under the **MIT License** — free to use with attribution.


## 🤝 Contributing

Contributions are welcome!  
If you want to help improve the dictionary or translation model, feel free to open an **issue** or submit a **pull request**.



## 📣 Acknowledgments

Special thanks to everyone supporting the promotion of African languages 🌍✨!


