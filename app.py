import streamlit as st
import random
import time
import os

# Arabic letters with pronunciation files
arabic_letters = {
    "ا": "sounds/ا.mp3", "ب": "sounds/ب.mp3", "ت": "sounds/ت.mp3", "ث": "sounds/ث.mp3",
    "ج": "sounds/ج.mp3", "ح": "sounds/ح.mp3", "خ": "sounds/خ.mp3", "د": "sounds/د.mp3",
    "ذ": "sounds/ذ.mp3", "ر": "sounds/ر.mp3", "ز": "sounds/ز.mp3", "س": "sounds/س.mp3",
    "ش": "sounds/ش.mp3", "ص": "sounds/ص.mp3", "ض": "sounds/ض.mp3", "ط": "sounds/ط.mp3",
    "ظ": "sounds/ظ.mp3", "ع": "sounds/ع.mp3", "غ": "sounds/غ.mp3", "ف": "sounds/ف.mp3",
    "ق": "sounds/ق.mp3", "ك": "sounds/ك.mp3", "ل": "sounds/ل.mp3", "م": "sounds/م.mp3",
    "ن": "sounds/ن.mp3", "ه": "sounds/ه.mp3", "و": "sounds/و.mp3", "ي": "sounds/ي.mp3"
}

# Harakat (diacritics)
harakat = {
    "َ": "fatha", "ِ": "kasra", "ُ": "damma", "ْ": "sukoon",
    "ّ": "shadda", "ً": "tanween_fath", "ٍ": "tanween_kasr", "ٌ": "tanween_damm"
}

# Words from the Quran with translations
words_data = {
    "بِسْمِ": {"english": "In the name of", "dutch": "In de naam van", "audio": "sounds/bismillah.mp3"},
    "اللَّهُ": {"english": "Allah", "dutch": "Allah", "audio": "sounds/allah.mp3"},
    "الرَّحْمٰنِ": {"english": "The Most Gracious", "dutch": "De Meest Barmhartige", "audio": "sounds/ar-rahman.mp3"},
    "الرَّحِيْمِ": {"english": "The Most Merciful", "dutch": "De Meest Genadevolle", "audio": "sounds/ar-raheem.mp3"},
}

# Function to get a list of unique random Arabic letters
def get_unique_random_letters(level, count):
    available_letters = list(arabic_letters.keys())
    random.shuffle(available_letters)
    selected_letters = available_letters[:count]
    return [(letter, arabic_letters[letter]) for letter in selected_letters]

# Function to get a list of unique random words
def get_unique_random_words(count):
    available_words = list(words_data.keys())
    random.shuffle(available_words)
    selected_words = available_words[:count]
    return [(word, words_data[word]["audio"], words_data[word]["english"], words_data[word]["dutch"]) for word in selected_words]

# Function to play audio automatically
def play_audio(audio_file, key):
    if os.path.exists(audio_file):
        try:
            st.audio(audio_file, format="audio/mp3", key=key)
            return True
        except Exception as e:
            st.warning(f"⚠️ Fout bij het afspelen van audio: {e}")
            return False
    else:
        return False

# Streamlit UI
st.title("📖 Leer Arabische Letters en Woorden 🎧")
st.subheader("🔠 Train je uitspraak en herkenning")

# Choice between letters and words
choice = st.radio("Wil je letters of woorden oefenen?", ["Letters", "Woorden"])

# Select difficulty level
level = st.radio("Kies een niveau:", ["Beginner", "Medior", "Advanced"])

if st.button("Start oefening"):
    unique_key = 0  # Key counter to avoid duplicate Streamlit elements
    
    if choice == "Letters":
        exercises = get_unique_random_letters(level, 15)
    else:
        exercises = get_unique_random_words(15)
    
    for item in exercises:
        st.empty()  # Verwijder vorige letter/woord
        placeholder = st.empty()
        unique_key += 1
        
        if choice == "Letters":
            letter, audio_file = item
            placeholder.markdown(f"<h1 style='font-size:80px; text-align:center;'>{letter}</h1>", unsafe_allow_html=True)
        else:
            word, audio_file, english_meaning, dutch_meaning = item
            placeholder.markdown(f"<h1 style='font-size:80px; text-align:center;'>{word}</h1>", unsafe_allow_html=True)
            st.markdown(f"<h3 style='text-align:center;'>Engels: {english_meaning}</h3>", unsafe_allow_html=True)
            st.markdown(f"<h3 style='text-align:center;'>Nederlands: {dutch_meaning}</h3>", unsafe_allow_html=True)
        
        time.sleep(5)  # Laat het woord/letter 4 seconden zien
        
        if play_audio(audio_file, f"audio_{unique_key}"):
            time.sleep(2)  # Wacht 2 seconden na audio voordat de volgende verschijnt
        
        placeholder.empty()  # Verwijder het vorige item voordat de volgende verschijnt

st.info("💡 Probeer hardop mee te spreken!")
