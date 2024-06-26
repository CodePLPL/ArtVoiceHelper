import speech_recognition as sr
import keyboard
import os
import json 
import webbrowser
import datetime
import requests
import screen_brightness_control as sbc # type: ignore
from openai import OpenAI
from gtts import gTTS
from pydub.playback import play
from pydub import AudioSegment
from datetime import datetime
##Импортируемые библиотеки

if os.path.exists('checktoken.txt'):
    pass
else:
    os.startfile(r'configure.bat')
    with open("checktoken.txt", "w") as write_file:
        write_file.write("Checking is complete")

r = sr.Recognizer() ## Подключение обработчика
mic = sr.Microphone() ## Подключение микрофона
sr.LANGUAGE = 'ru-RU' ## Язык обработки

def console_Art():
    print(" ##   ####   ####")
    print("#  #  #  #    # ")
    print("####  ###     # ")
    print("#  #  #  #    # ")

console_Art()

print("\033[33m" + "ART (automator of routine tasks)" + "\033[0m")
print("\033[33m" + "Это мой школьный проект. Я постарался в нем показать мои способности в программировании. Кроме того, это мой первый проект. Буду рад, если вы оцените его" + "\033[0m")
print("\033[33m" + "Для запуска программы у вас должен быть установлен python, если у вас возникают проблемы в работе программы то возможно вы словили баг. Если у вас возникают проблемы при работе с ии, то вероятнее всего сервера OpenAi не доступны" + "\033[0m")
print("\033[33m" + "This is my school project. I tried to show my programming abilities in it. Besides, this is my first project. I will be glad if you rate it" + "\033[0m")
print("\033[33m" + "To run the program, you must have python installed; if you have problems with the program, you may have caught a bug. If you have problems working with AI, then most likely the OpenAi servers are not available" + "\033[0m")
print("Вы можете поддержать проект криптой BTC:1CVLhwWgHxoEciQTjZsxTQh6yd92PAmpjp, ETH:0x883909cdBD6A9B6f6CDBfa9118A45E41c3b06fBc;\nYou can support the project with crypto: BTC:1CVLhwWgHxoEciQTjZsxTQh6yd92PAmpjp, ETH:0x883909cdBD6A9B6f6CDBfa9118A45E41c3b06fBc")
print("__________________________________________")

print("\033[31m" + "Для обычного вызова нажмите 'left alt', для ии вызова нажмите 'left ctrl', чтобы выйти из программы скажите 'остановка' или нажмите 'Esc';\nFor a normal call, press 'left alt', for a normal call, press 'left ctrl', to exit the program press 'Esc'" + "\033[0m")

if os.path.exists('data.json'):
    with open("data.json", "r") as read_file:
        data = json.load(read_file)
else:
    with open("data.json", "w") as write_file:
        print("Введите ваш ключ Api OpenAI:")
        api_key = input()
        print("Введите ваш ключ каталога Yandex:")
        catalog_word = input()
        print("Введите ваш ключ Api Yandex:")
        Api_word = input()
        print("С какой нейросетью вы хотите работать: 1 - gpt-3.5-turbo, 2 - yandex_gpt")
        gpt_num = input()
        data = dict({'ApiKey' : api_key, 'Yandex-ApiKey': Api_word, 'Yandex-Catalog': catalog_word})
        json.dump(data, write_file)
## Файл данных
catalog_id = data['Yandex-Catalog']
Yandex_api_key = data['Yandex-ApiKey']
gpt_num = int(data['gpt_num'])

Recs = AudioSegment.from_mp3('RecS.mp3')
RecEr = AudioSegment.from_mp3('RecEr.mp3')
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
            elif text == "Включи музыку":
                webbrowser.open("https://music.yandex.ru/home")
            elif text == "открой переводчик":
                webbrowser.open("https://translate.google.com/?hl=ru")
            elif text == "Открой почту":
                webbrowser.open("https://mail.google.com")
            elif text == "Очисти логи":
                os.system('cls')
            elif "яркость" in text:
                length = len(text)
                integers = []
                i = 0
                while i < length:
                    s_int = ''
                    while i < length and '0' <= text[i] <= '9':
                        s_int += text[i]
                        i += 1
                    i += 1
                    if s_int != '':
                        integers.append(float(s_int))
                i = 0
                print(s_int)
                sbc.set_brightness(s_int)
            elif text == "Какой сегодня день":
                print("Формат вывода даты: день, месяц, год")
                current_datetime = datetime.now().date().strftime("%d, %m, %Y")
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
                play(RecEr)
                continue  
        elif keyboard.is_pressed('left ctrl') and gpt_num == 2:
            
            with mic as source:
                r.adjust_for_ambient_noise(source)
                play(Recs)
                audio = r.listen(source)
            text = r.recognize_google(audio, language='ru-RU')
            print(text)
            try:
                text = str(text)
                Yandex_api_key = str(Yandex_api_key)
                catalog_id = str(catalog_id)
                prompt = {
                    "modelUri": f"gpt://{catalog_id}/yandexgpt-lite",
                    "completionOptions": {
                        "stream": False,
                        "temperature": 0.6,
                        "maxTokens": "2000"
                    },
                    "messages": [
                        {
                            "role": "system",
                            "text": "Ты ассистент работающий на компьютере программиста"
                        },
                        {
                            "role": "user",
                            "text": text
                        }
                    ]
                }


                url = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"
                headers = {
                    "Content-Type": "application/json",
                    "Authorization": f"Api-Key {Yandex_api_key}"
                }

                response = requests.post(url, headers=headers, json=prompt)
                result = response.text
                print(result)
            except:
                play(RecEr)
                print("К сожалению возникла проблема с api Yandex, попробуйте другой ключ, проверте доступность серверов Yandex и повторите попытку")

        elif keyboard.is_pressed('left ctrl') and gpt_num == 1:        
            with mic as source:
                r.adjust_for_ambient_noise(source)
                play(Recs)
                audio = r.listen(source)
            text = r.recognize_google(audio, language='ru-RU')
            print(text)
            try:
                   
                client = OpenAI(api_key = data['ApiKey'])

                stream = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": text}],
                    stream=True,
                    )
                print("<</")
                for chunk in stream:
                    if chunk.choices[0].delta.content is not None:
                        print(chunk.choices[0].delta.content, end="")
                print("/>>")
            except:
                play(RecEr)
                print("К сожалению возникла проблема с api OpenAi, попробуйте другой ключ, проверте доступность серверов OpenAi и повторите попытку")   
        elif keyboard.is_pressed('esc'):
            break            
        else:
            continue
    except:
        play(RecEr)
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