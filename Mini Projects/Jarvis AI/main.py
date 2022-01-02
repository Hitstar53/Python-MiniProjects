#jarvis ai project
#importing libraries
import pyttsx3
import speech_recognition as sr
from datetime import datetime
from decouple import config
import random
from utils import opening_text

#setup
USERNAME = config('USER')
BOTNAME = config('BOTNAME')

engine = pyttsx3.init('sapi5')
#set rate
rate = engine.setProperty('rate',190)
#set volume
volume = engine.setProperty('volume',1.0)
#set voice (female)
voices = engine.getProperty('voices')
voice = engine.setProperty('voice',voices[0].id)

#text to speech conversion
def speak(text):
    engine.say(text)
    engine.runAndWait()

#greet function
def greet():
    hour = int(datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak(f"Good Morning! {USERNAME}")
    elif hour >= 12 and hour < 18:
        speak(f"Good Afternoon! {USERNAME}")
    else:
        speak(f"Good Evening! {USERNAME}")
    speak("I am "+ BOTNAME + " How may I help you?")

#take user input
def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source=source)
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        if not 'exit' in query or 'stop' in query:
            speak(random.choice(opening_text))
        else:
            hour = datetime.now().hour
            if hour >= 21 and hour < 6:
                speak("Good Night sir, Take Care!")
            else:
                speak("Have a Good day sir!")
            exit()
    except Exception:
        speak('Sorry sir, I could not understand. Could you say that Again?')
        query = None
    return query

#importing commands
from commands.online_ops import *
from commands.os_ops import *
from pprint import pprint

if __name__ == '__main__':
    greet()
    while True:
        query = take_command().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace('wikipedia','')
            results = search_on_wikipedia(query)
            speak(results)
        elif 'open youtube' in query:
            speak('Opening Youtube...')
            query = query.replace('open youtube','')
            play_on_youtube(query)
        elif 'open google' in query:
            speak('Opening Google...')
            query = query.replace('open google','')
            search_on_google(query)
        elif 'play music' in query:
            speak('Playing Music...')
            query = query.replace('play music','')
            play_on_youtube(query)
        elif 'send whatsapp' in query:
            speak('Sending Whatsapp...')
            query = query.replace('send whatsapp','')
            number,message = query.split('-')
            send_whatsapp_message(number,message)
        elif 'send email' in query:
            speak('Sending Email...')
            query = query.replace('send email','')
            receiver_address,subject,message = query.split('-')
            send_email(receiver_address,subject,message)
        elif 'send message' in query:
            speak('Sending Message...')
            query = query.replace('send message','')
            number,message = query.split('-')
            send_whatsapp_message(number,message)
        elif 'open' in query:
            query = query.replace('open','')
            if 'notepad' in query:
                open_notepad()
            elif 'chrome' in query:
                open_chrome()
            elif 'discord' in query:
                open_discord()
            elif 'cmd' in query:
                open_cmd()
            elif 'calculator' in query:
                open_calculator()
            elif 'camera' in query:
                open_camera()
            else:
                speak('Sorry sir, I could not understand. Could you say that Again?')
        elif 'exit' in query:
            speak('Have a Good day sir!')
            exit()
