import speech_recognition as sr
import pyttsx3
import os
import subprocess
import webbrowser
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

# Инициализация синтеза речи
engine = pyttsx3.init()
recognizer = sr.Recognizer()
microphone = sr.Microphone()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with microphone as source:
        print("Слушаю...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        query = recognizer.recognize_google(audio, language="ru-RU")
        print(f"Вы сказали: {query}")
        return query.lower()
    except:
        return ""

def set_volume(level):
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    volume.SetMasterVolumeLevelScalar(level / 100, None)

def handle_command(command):
    if "привет" in command:
        speak("Здравствуйте! Чем могу помочь?")
    elif "открой браузер" in command:
        webbrowser.open("https://google.com")
        speak("Браузер открыт.")
    elif "выключи компьютер" in command:
        os.system("shutdown /s /t 1")
    elif "громкость" in command:
        if "увеличь" in command:
            set_volume(80)
            speak("Громкость увеличена.")
        elif "уменьши" in command:
            set_volume(20)
            speak("Громкость уменьшена.")
    elif "пока" in command:
        speak("До свидания!")
        exit()
    else:
        speak("Команда не распознана.")

if __name__ == "__main__":
    speak("Ассистент запущен.")
    while True:
        command = listen()
        if command:
            handle_command(command)
