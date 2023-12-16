import speech_recognition as sr
import keyboard
import os
import json ##Импортируемые библиотеки
import webbrowser
from gtts import gTTS
from pydub.playback import play
from pydub import AudioSegment

r = sr.Recognizer() ## Подключение обработчика
mic = sr.Microphone() ## Подключение микрофона

sr.LANGUAGE = 'ru-RU' ## Язык обработки

if os.path.exists('data.json'):
    with open("data.json", "r") as read_file:
        data = json.load(read_file)
else:
    with open("data.json", "w") as write_file:
        print("Введите своё имя")
        name = input()
        print("Введите свою фамилию")
        surname = input()
        data = dict({'Name' : name, 'SName': surname})
        json.dump(data, write_file)
## Файл данных
name = data.get('Name')
tts = gTTS("Я приветствую вас, чем я могу вам помочь", lang='ru')
tts.save('hello.mp3')
HelloA = AudioSegment.from_mp3('hello.mp3')
play(HelloA)



"""
while True:
    if keyboard.is_pressed('left alt'):
        with mic as source:
            r.adjust_for_ambient_noise(source)
            print("Запись Пошла")
            audio = r.listen(source)
        text = r.recognize_google(audio, language='ru-RU')
        print(text)
        if text == "остановка":
            break
        elif text == "Открой проводник":
            os.system("explorer.exe")      
        else:
            print("К сожалению я не понял вас")
            continue
"""

while True:
    try:
        with mic as source:
                r.adjust_for_ambient_noise(source)
                print("∏")
                audio = r.listen(source)
        voicename = r.recognize_google(audio, language='ru-RU')
        print(voicename)
        if voicename == "Привет арт":
            with mic as source:
                r.adjust_for_ambient_noise(source)
                print("Запись Пошла")
                audio = r.listen(source)
            text = r.recognize_google(audio, language='ru-RU')
            print(text)
            if text == "остановка":
                break
            elif text == "Открой проводник":
                os.system("explorer.exe")   
            elif text == "Открой браузер":
                webbrowser.open("https://www.google.ru/?hl=ru")     
            elif text == "Открой YouTube":
                webbrowser.open("https://www.youtube.com/")
            elif text == "открой github":
                webbrowser.open("https://github.com/")
            elif text == "Очисти логи":
                os.system('cls')                
            else:
                print("К сожалению я не понял вас")
                continue
        else:
            continue
    except:
        continue

# Очистка лишних данных     
if os.path.exists('hello.mp3'):
    os.remove('hello.mp3')