# Generar audios de números coreanos del 1 al 10 y del 10 en 10 hasta 100
# usando gTTS (Google Text-to-Speech)

from gtts import gTTS
import os

# Crear carpeta 'audio' si no existe
if not os.path.exists("audio"):
    os.makedirs("audio")

# Diccionario de números coreanos
numeros = {
    "hana": "하나",
    "dul": "둘",
    "set": "셋",
    "net": "넷",
    "daseot": "다섯",
    "yeoseot": "여섯",
    "ilgop": "일곱",
    "yeodeol": "여덟",
    "ahop": "아홉",
    "yeol": "열",
    "seumul": "스물",
    "seoreun": "서른",
    "maheun": "마흔",
    "swin": "쉰",
    "yesun": "예순",
    "ilheun": "일흔",
    "yeodeun": "여든",
    "aheun": "아흔",
    "baek": "백"
}

# Generar y guardar cada audio
for nombre, hangul in numeros.items():
    tts = gTTS(text=hangul, lang='ko')
    archivo = f"audio/{nombre}.mp3"
    tts.save(archivo)
    print(f"Generado: {archivo}")

print("¡Todos los audios se han generado en la carpeta 'audio'!")