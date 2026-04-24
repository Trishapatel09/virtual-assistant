import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import time

myname = 'your well wisher'

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = datetime.datetime.now().hour

    if hour < 12:
        speak(f'Good morning , I am {myname}. How may I help you?')
    elif hour < 18:
        speak(f'Good afternoon , I am {myname}. How may I help you?')
    else:
        speak(f'Good evening , I am {myname}. How may I help you?')


def hearme():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        audio = r.listen(source)
    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-IN')
        print('You said:', query)
    except Exception:
        print('Say that again please...')
        return ""

    return query


if __name__ == "__main__":
    wishme()
    last_query = ""

    while True:
        query = hearme()
        if not query:
            continue
        query = query.lower()
        if query == last_query:
            continue
        last_query = query

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace('wikipedia', '')
            try:
                result = wikipedia.summary(query, sentences=2)
                print(result)
                speak("According to Wikipedia " + result)
            except Exception:
                speak("Sorry, I couldn't find anything on Wikipedia.")

        elif 'how' in query:
            speak("I am fine, how can I help you?")

        elif 'help' in query:
            speak("Tell me what you need")

        elif 'hello' in query or 'hi' in query or 'hey' in query:
            speak("Hello, how can I help you?")

        elif 'google' in query:
            webbrowser.open('https://www.google.com')

        elif 'instagram' in query:
            webbrowser.open('https://www.instagram.com')

        elif 'chatgpt' in query:
            webbrowser.open('https://www.chatgpt.com')

        elif 'your pic' in query or 'your image' in query:
            os.startfile(f'https://www.google.com/search?q={query}')
        else:
            webbrowser.open('https://www.google.com/search?q=' + query)

        time.sleep(2)