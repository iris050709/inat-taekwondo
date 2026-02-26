from gtts import gTTS

taegeuk = {
    "taegeuk1": "Taegeuk Il Jang",
    "taegeuk2": "Taegeuk Yi Jang",
    "taegeuk3": "Taegeuk Sam Jang",
    "taegeuk4": "Taegeuk Sa Jang",
    "taegeuk5": "Taegeuk Oh Jang",
    "taegeuk6": "Taegeuk Yook Jang",
    "taegeuk7": "Taegeuk Chil Jang",
    "taegeuk8": "Taegeuk Pal Jang"
}

for key, text in taegeuk.items():
    tts = gTTS(text, lang='ko')  # Para pronunciación en coreano
    tts.save(f"audio/{key}.mp3")
    print(f"{key}.mp3 generado")