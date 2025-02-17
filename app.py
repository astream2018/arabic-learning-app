@@ -0,0 +1,123 @@
import uuid

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
    "بِسْمِ": {"english": "In the name of", "dutch": "In de naam van", "audio": "sounds/بِسْمِ.mp3"},
    "اللَّهُ": {"english": "Allah", "dutch": "Allah", "audio": "sounds/اللَّهُ.mp3"},
    "الرَّحْمٰنِ": {"english": "The Most Gracious", "dutch": "De Meest Barmhartige", "audio": "sounds/الرَّحْمٰنِ.mp3"},
    "الرَّحِيْمِ": {"english": "The Most Merciful", "dutch": "De Meest Genadevolle", "audio": "sounds/الرَّحِيْمِ.mp3"},
    "الْحَمْدُ": {"english": "Praise", "dutch": "Lof", "audio": "sounds/الْحَمْدُ.mp3"},
    "رَبِّ": {"english": "Lord", "dutch": "Heer", "audio": "sounds/رَبِّ.mp3"},
    "الْعَالَمِينَ": {"english": "The Worlds", "dutch": "De Werelden", "audio": "sounds/الْعَالَمِينَ.mp3"},
    "مَالِكِ": {"english": "Owner", "dutch": "Eigenaar", "audio": "sounds/مَالِكِ.mp3"},
    "يَوْمِ": {"english": "Day", "dutch": "Dag", "audio": "sounds/يَوْمِ.mp3"},
    "الدِّينِ": {"english": "Religion", "dutch": "Religie", "audio": "sounds/الدِّينِ.mp3"},
    "إِيَّاكَ": {"english": "You alone", "dutch": "Jou alleen", "audio": "sounds/إِيَّاكَ.mp3"},
    "نَعْبُدُ": {"english": "We worship", "dutch": "Wij aanbidden", "audio": "sounds/نَعْبُدُ.mp3"},
    "وَإِيَّاكَ": {"english": "And You alone", "dutch": "En jou alleen", "audio": "sounds/وَإِيَّاكَ.mp3"},
    "نَسْتَعِينُ": {"english": "We seek help", "dutch": "Wij zoeken hulp", "audio": "sounds/نَسْتَعِينُ.mp3"},
    "اهْدِنَا": {"english": "Guide us", "dutch": "Leid ons", "audio": "sounds/اهْدِنَا.mp3"},
    "الصِّرَاطَ": {"english": "The path", "dutch": "Het pad", "audio": "sounds/الصِّرَاطَ.mp3"},
    "الْمُسْتَقِيمَ": {"english": "The straight", "dutch": "Het rechte", "audio": "sounds/الْمُسْتَقِيمَ.mp3"},
    "الْجَنَّةُ": {"english": "Paradise", "dutch": "Paradijs", "audio": "sounds/الْجَنَّةُ.mp3"},
    "النَّارُ": {"english": "Hellfire", "dutch": "Hellevuur", "audio": "sounds/النَّارُ.mp3"},
    "الدُّنْيَا": {"english": "World", "dutch": "Wereld", "audio": "sounds/الدُّنْيَا.mp3"},
    "الْآخِرَةُ": {"english": "Hereafter", "dutch": "Hiernamaals", "audio": "sounds/الْآخِرَةُ.mp3"},
    "الْقُرْآنُ": {"english": "Quran", "dutch": "Koran", "audio": "الْقُرْآنُ.sounds/mp3"},
    "الْمُؤْمِنُونَ": {"english": "Believers", "dutch": "Gelovigen", "audio": "sounds/الْمُؤْمِنُونَ.mp3"},
    "النَّبِيُّ": {"english": "Prophet", "dutch": "Profeet", "audio": "sounds/النَّبِيُّ.mp3"},
    "الرَّسُولُ": {"english": "Messenger", "dutch": "Boodschapper", "audio": "sounds/الرَّسُولُ.mp3"}
}


# Function to get a random Arabic letter
def get_random_letter(level):
    base_letter = random.choice(list(arabic_letters.keys()))

    if level == "Beginner":
        return base_letter, arabic_letters[base_letter]
    elif level == "Medior":
        diacritic = random.choice(list(harakat.keys()))
        return base_letter + diacritic, f"sounds/{base_letter}_{harakat[diacritic]}.mp3"
    elif level == "Advanced":
        word = random.choice(list(words_data.keys()))
        return word, words_data[word]["audio"]
    return base_letter, arabic_letters[base_letter]


# Function to get a random word from the Quran
def get_random_word():
    word = random.choice(list(words_data.keys()))
    return word, words_data[word]["audio"], words_data[word]["english"], words_data[word]["dutch"]


# Function to play audio automatically with a unique key
def play_audio(audio_file):
    if os.path.exists(audio_file):
        st.empty()  # Clear any previous audio elements
        st.audio(audio_file, format="audio/mp3", autoplay=True)
        return True
    else:
        st.error(f"❌ Audio bestand niet gevonden: {audio_file}")
        return False




# Streamlit UI
st.title("📖 Leer Arabische Letters en Woorden 🎧")
st.subheader("🔠 Train je uitspraak en herkenning")

# Choice between letters and words
choice = st.radio("Wil je letters of woorden oefenen?", ["Letters", "Woorden"])

# Select difficulty level
level = st.radio("Kies een niveau:", ["Beginner", "Medior", "Advanced"])

if st.button("Start oefening"):
    for i in range(15):
        st.empty()  # Clear previous letter/word

        if choice == "Letters":
            letter, audio_file = get_random_letter(level)
            placeholder = st.empty()
            placeholder.markdown(f"<h1 style='font-size:80px; text-align:center;'>{letter}</h1>",
                                 unsafe_allow_html=True)
        else:
            word, audio_file, english_meaning, dutch_meaning = get_random_word()
            placeholder = st.empty()
            placeholder.markdown(f"<h1 style='font-size:80px; text-align:center;'>{word}</h1>", unsafe_allow_html=True)
            st.markdown(f"<h3 style='text-align:center;'>Engels: {english_meaning}</h3>", unsafe_allow_html=True)
            st.markdown(f"<h3 style='text-align:center;'>Nederlands: {dutch_meaning}</h3>", unsafe_allow_html=True)

        time.sleep(4)  # Display the letter/word for 4 seconds

        if play_audio(audio_file):
            time.sleep(2)  # Wait 2 seconds after audio before showing the next one

        placeholder.empty()  # Clear the UI before displaying the next one
        st.empty()

st.info("💡 Probeer hardop mee te spreken!")
