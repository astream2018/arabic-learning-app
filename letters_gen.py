from gtts import gTTS
import os

# Maak een map voor de audio
audio_dir = "sounds"
if not os.path.exists(audio_dir):
    os.mkdir(audio_dir)

# Arabische letters en diacritical marks (Harakat)
arabic_letters = [
    "ا", "ب", "ت", "ث", "ج", "ح", "خ", "د", "ذ", "ر", "ز", "س", "ش", "ص", "ض",
    "ط", "ظ", "ع", "غ", "ف", "ق", "ك", "ل", "م", "ن", "ه", "و", "ي"
]

harakat = {
    "َ": "fatha",
    "ِ": "kasra",
    "ُ": "damma",
    "ْ": "sukoon",
    "ّ": "shadda",
    "ً": "tanween_fath",
    "ٍ": "tanween_kasr",
    "ٌ": "tanween_damm"
}

# Genereer en sla MP3-bestanden op voor basisletters
for letter in arabic_letters:
    tts = gTTS(text=letter, lang="ar")
    filename = os.path.join(audio_dir, f"{letter}.mp3")
    tts.save(filename)
    print(f"✅ Opgeslagen: {filename}")

# Genereer en sla MP3-bestanden op voor letters met Harakat
for letter in arabic_letters:
    for haraka, haraka_name in harakat.items():
        letter_with_haraka = letter + haraka
        filename = os.path.join(audio_dir, f"{letter}_{haraka_name}.mp3")
        tts = gTTS(text=letter_with_haraka, lang="ar")
        tts.save(filename)
        print(f"✅ Opgeslagen: {filename}")

print("🎉 Alle audiobestanden zijn gegenereerd en opgeslagen in de 'sounds/' map!")
