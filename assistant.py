# CREDIT for GLaDOS voices goes to 15.ai & Ellen McLain

#import speech_recognition as sr
from playsound import playsound
import webbrowser
from gtts import gTTS
import os
import random
import time
from datetime import date
from datetime import datetime
import pyautogui
import sys

audio_path = os.path.join(os.path.dirname(__file__), 'audio')

playsound(os.path.join(audio_path, 'intro.mp3')
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
            pass
        except sr.RequestError:
            playsound(os.path.join(audio_path, 'offline.mp3')
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
        playsound(os.path.join(audio_path, 'hello.mp3')

    elif 'hello' in voice_data:
        playsound(os.path.join(audio_path, 'hello.mp3')

    elif 'name' in voice_data:
        playsound(os.path.join(audio_path, 'glados_name.mp3')

    elif 'who are you' in voice_data:
        playsound(os.path.join(audio_path, 'glados_name.mp3')

    elif "thank you" in voice_data:
        playsound(os.path.join(audio_path, 'you_welcome.mp3')

    elif "thanks" in voice_data:
        playsound(os.path.join(audio_path, 'you_welcome.mp3')

    elif 'time' in voice_data:
        t = time.strftime("%I:%M %p")
        glados_speak(t)

    elif 'date' in voice_data:
        today = date.today()
        date_today = today.strftime("%b-%d-%Y")
        glados_speak(date_today)

    elif 'search for' in voice_data:
        search_term = voice_data.split("search for")[-1]
        url = "https://google.com/search?q=" + search_term
        playsound(os.path.join(audio_path, 'searching.mp3')
        webbrowser.get()
        webbrowser.open(url)
        playsound(os.path.join(audio_path, '_found.mp3')

    elif 'potato' in voice_data:
        playsound(os.path.join(audio_path, 'potato.mp3')

    elif 'oh' in voice_data:
        playsound(os.path.join(audio_path, 'dead.mp3')

    elif 'screenshot' in voice_data:
        rand = str(random.randint(1, 1000))
        myScreenshot = pyautogui.screenshot(f'{rand}.png')
        playsound(os.path.join(audio_path, 'screenshot_taken.mp3')

    elif 'sneeze' in voice_data:
        playsound(os.path.join(audio_path, 'sneeze.mp3')

    elif 'tell me something funny' in voice_data:
        playsound(os.path.join(audio_path, '_adopted.mp3')

    elif 'google' in voice_data:
        os.startfile('C:\\Users\\Public\\Desktop\\Google Chrome.lnk')
        playsound(os.path.join(audio_path, 'program.mp3')

    elif 'battlefield' in voice_data:
        os.startfile('C:\\Users\Matth\\OneDrive\\Desktop\\Battlefield™ 2042.url')
        playsound(os.path.join(audio_path, 'program.mp3')

    elif 'steam' in voice_data:
        os.startfile('C:\\Users\\Public\Desktop\\Steam.lnk')
        playsound(os.path.join(audio_path, 'program.mp3')

    elif 'rust' in voice_data:
        os.startfile("C:\\Users\\Matth\\OneDrive\\Desktop\\Rust.url")
        playsound(os.path.join(audio_path, 'program.mp3')
        
    elif 'christmas' in voice_data:
        playsound(os.path.join(audio_path, 'christmas.mp3')

    elif 'holidays' in voice_data:
        playsound(os.path.join(audio_path, 'holidays.mp3')

    elif 'bye' in voice_data:
        playsound(os.path.join(audio_path, 'Bye.mp3')

    else:
        if 'exit' in voice_data:
            playsound(os.path.join(audio_path, 'exiting.mp3')
            sys.exit()
            
while True:
    voice_data = record_audio()
    respond(voice_data)
