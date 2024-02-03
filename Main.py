import speech_recognition as sr
import keyboard
import os
import json ##Импортируемые библиотеки
import webbrowser
import datetime
import requests
import openai
from gtts import gTTS
from pydub.playback import play
from pydub import AudioSegment
from datetime import datetime

r = sr.Recognizer() ## Подключение обработчика
mic = sr.Microphone() ## Подключение микрофона

openai.api_key = "" # Ввод ключа OpenAI
model_engine = "text-davinci-003"
max_tokens = 128

sr.LANGUAGE = 'ru-RU' ## Язык обработки

if os.path.exists('data.json'):
    with open("data.json", "r") as read_file:
        data = json.load(read_file)
else:
    with open("data.json", "w") as write_file:
        api_key = input()
        data = dict({'ApiKey' : api_key})
        json.dump(data, write_file)
## Файл данных
name = data.get('Name')
tts = gTTS("Я приветствую вас, чем я могу вам помочь", lang='ru')
tts.save('hello.mp3')
HelloA = AudioSegment.from_mp3('hello.mp3')
play(HelloA)
Recs = AudioSegment.from_mp3('RecS.mp3')

while True:
    try:
        if keyboard.is_pressed('left alt'):
            with mic as source:
                r.adjust_for_ambient_noise(source)
                play(Recs)
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
            elif text == "Какой сегодня день":
                print("Формат вывода даты: год, месяц, день")
                current_datetime = datetime.now().date()
                current_datetime_str = str(current_datetime)
                tts = gTTS(current_datetime_str, lang='ru')
                tts.save('datetime.mp3')
                DataTime = AudioSegment.from_mp3('datetime.mp3')
                play(DataTime)
            elif text == "статус сети":
                if requests.get('https://www.youtube.com/').ok:
                    tts = gTTS("Соединение стабильное", lang='ru')
                    tts.save('StatusOk.mp3')
                    StatusWeb = AudioSegment.from_mp3('StatusOk.mp3')
                    play(StatusWeb)
                else:
                    tts = gTTS("Соединение нестабильное", lang='ru')
                    tts.save('StatusNO.mp3')
                    StatusWeb = AudioSegment.from_mp3('StatusNO.mp3')
                    play(StatusWeb)
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
if os.path.exists('datetime.mp3'):
    os.remove('datetime.mp3')
if os.path.exists('StatusOk.mp3'):
    os.remove('StatusOk.mp3')
if os.path.exists('StatusNO.mp3'):
    os.remove('StatusNO.mp3')