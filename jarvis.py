from email.mime import audio
from re import S
from unicodedata import name
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
print(voices[2].id)
engine.setProperty('voice',voices[2].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour=int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:
        speak("Good morning sir!!")
    elif hour>=12 and hour < 18:
        speak ("Good afternoon sir!!")
    else:
        speak("Good evening sir!!")
    speak("Sir, i am jarvis , Tell me what do you want , I am your personal assistant")
def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:

        print("Listening")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language="en-in")
        print(f"User said {query}/n")
    except Exception as e:
        print("Say that again...")
        return "None"
    return query
##def sendmail(to,content):
   ## s
if __name__=="__main__":
    wishme()
    while True:
        query=takecommand().lower()
        print(query)
        if 'wikipedia' in query:
            print('searching in wikipedia')
            query=query.replace('wikipedia','')
            results=wikipedia.summary(query,sentences=2)
            speak('According to wikipedia: ')
            print(results)
            speak(results)
        elif 'open youtube' in query:
            speak('opening sir')
            webbrowser.open('www.youtube.com')
        elif 'open google' in query:
            speak('searching sir')
            webbrowser.open('www.google.com')
        elif 'open instagram' in query:
            speak('opening sir')
            webbrowser.open('www.instagram.com')
        elif 'play music' in query:
            musicpath="D:\songs"
            songs=os.listdir(musicpath)
            print(songs)
            os.startfile(os.path.join(musicpath,songs[1]))
        elif 'the time' in query:
            strtime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(strtime)
            print(strtime)
        elif 'open code' in query:
            path="C:\\Users\\pavilion\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(path)
            speak('opening visual studio code')
        # elif 'send mail to harry' in query:
        #     speak('sending mail to harry')
        #     to='harrymail@gmail.com'
        #     content='What the fucj are u doing harry'
        #     sendmail(to,content)
        #     speak('mail sent')
            




            
            


