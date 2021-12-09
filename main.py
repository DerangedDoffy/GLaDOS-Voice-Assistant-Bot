# CREDIT for GLaDOS voices goes to 15.ai & Ellen McLain

import speech_recognition as sr
from playsound import playsound
import webbrowser
from gtts import gTTS
import os
import random
import time
from datetime import date
from datetime import datetime
import pyautogui

playsound('D:\Py Projects\Projects\GLaDOS\sound_files\intro.mp3')

r = sr.Recognizer()

r.energy_threshold = 4000


def record_audio(ask=False):

    with sr.Microphone() as source:
        if ask:
            glados_speak(ask)

        audio = r.listen(source)
        voice_data = ''

        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            time.sleep(60)
            playsound('D:\Py Projects\Projects\GLaDOS\sound_files\wheately.mp3')
        except sr.RequestError:
            playsound('D:\Py Projects\Projects\GLaDOS\sound_files\offline.mp3')
        print(f">>> {voice_data.lower()}")
        return voice_data.lower()


def glados_speak(audio_string):

    tts = gTTS(text=audio_string, lang='en')
    rand = random.randint(1, 1000000)
    audio_file = 'audio-' + str(rand) + '.mp3'
    tts.save(audio_file)
    playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)


def respond(voice_data):

    if 'hi' in voice_data:
        playsound('D:\Py Projects\Projects\GLaDOS\sound_files\hello.mp3')

    if 'hello' in voice_data:
        playsound('D:\Py Projects\Projects\GLaDOS\sound_files\hello.mp3')

    if 'name' in voice_data:
        playsound('D:\Py Projects\Projects\GLaDOS\sound_files\glados_name.mp3')

    if 'who are you' in voice_data:
        playsound('D:\Py Projects\Projects\GLaDOS\sound_files\glados_name.mp3')

    if 'what are you' in voice_data:
        playsound('D:\Py Projects\Projects\GLaDOS\sound_files\glados_name.mp3')

    if 'time' in voice_data:
        t = time.strftime("%I:%M %p")
        glados_speak(t)

    if 'date' in voice_data:
        today = date.today()
        date_today = today.strftime("%b-%d-%Y")
        glados_speak(date_today)

    if 'search for' in voice_data:
        search_term = voice_data.split("search for")[-1]
        url = "https://google.com/search?q=" + search_term
        playsound('D:\Py Projects\Projects\GLaDOS\sound_files\searching.mp3')
        webbrowser.get()
        webbrowser.open(url)
        playsound('D:\Py Projects\Projects\GLaDOS\sound_files\_found.mp3')
    if 'what does' in voice_data:
        search_term = voice_data
        url = "https://google.com/search?q=" + search_term
        playsound('D:\Py Projects\Projects\GLaDOS\sound_files\searching.mp3')
        webbrowser.get()
        webbrowser.open(url)
        playsound('D:\Py Projects\Projects\GLaDOS\sound_files\search_results.mp3')
    if 'who is' in voice_data:
        search_term = voice_data
        url = "https://google.com/search?q=" + search_term
        playsound('D:\Py Projects\Projects\GLaDOS\sound_files\searching.mp3')
        webbrowser.get()
        webbrowser.open(url)
        playsound('D:\Py Projects\Projects\GLaDOS\sound_files\search_results.mp3')
    if 'what is' in voice_data:
        search_term = voice_data
        url = "https://google.com/search?q=" + search_term
        playsound('D:\Py Projects\Projects\GLaDOS\sound_files\_found.mp3')
        webbrowser.get()
        webbrowser.open(url)
        playsound('D:\Py Projects\Projects\GLaDOS\sound_files\search_results.mp3')
    if 'how did' in voice_data:
        search_term = voice_data
        url = "https://google.com/search?q=" + search_term
        playsound('D:\Py Projects\Projects\GLaDOS\sound_files\searching.mp3')
        webbrowser.get()
        webbrowser.open(url)
        playsound('D:\Py Projects\Projects\GLaDOS\sound_files\search_results.mp3')
    if 'why did' in voice_data:
        search_term = voice_data
        url = "https://google.com/search?q=" + search_term
        playsound('D:\Py Projects\Projects\GLaDOS\sound_files\searching.mp3')
        webbrowser.get()
        webbrowser.open(url)
        playsound('D:\Py Projects\Projects\GLaDOS\sound_files\_found.mp3')

    if 'potato' in voice_data:
        playsound('D:\Py Projects\Projects\GLaDOS\sound_files\potato.mp3')

    if 'bye' in voice_data:
        playsound('D:\Py Projects\Projects\GLaDOS\sound_files\Bye.mp3')

    if 'miss' in voice_data:
        playsound('D:\Py Projects\Projects\GLaDOS\sound_files\dead.mp3')

    if 'oh' in voice_data:
        playsound('D:\Py Projects\Projects\GLaDOS\sound_files\dead.mp3')

    if 'exit' in voice_data:
        playsound('D:\Py Projects\Projects\GLaDOS\sound_files\exiting.mp3')
        quit()

    if 'leave' in voice_data:
        playsound('D:\Py Projects\Projects\GLaDOS\sound_files\exiting.mp3')
        quit()

    if 'shut up' in voice_data:
        playsound('D:\Py Projects\Projects\GLaDOS\sound_files\exiting.mp3')
        quit()

    if 'quiet' in voice_data:
        playsound('D:\Py Projects\Projects\GLaDOS\sound_files\exiting.mp3')
        quit()

    if 'screenshot' in voice_data:
        rand = str(random.randint(1, 1000))
        myScreenshot = pyautogui.screenshot(f'{rand}.png')
        playsound('D:\Py Projects\Projects\GLaDOS\sound_files\screenshot_taken.mp3')

    if 'sneeze' in voice_data:
        playsound('D:\Py Projects\Projects\GLaDOS\sound_files\sneeze.mp3')

    if 'plus' in voice_data:
        #playsound('D:\Py Projects\Projects\GLaDOS\sound_files\easy_math.mp3')
        pass

    if 'adopted' in voice_data:
        playsound('D:\Py Projects\Projects\GLaDOS\sound_files\_adopted.mp3')

    if 'funny' in voice_data:
        playsound('D:\Py Projects\Projects\GLaDOS\sound_files\_adopted.mp3')


time.sleep(1)

while 1:
    voice_data = record_audio()
    respond(voice_data)
