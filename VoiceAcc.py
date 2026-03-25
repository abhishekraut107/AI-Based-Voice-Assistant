import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import wikipedia

import speech_recognition as sr

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        query = r.recognize_google(audio)
        return query


engine = pyttsx3.init()

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def take_command():
    listener = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = listener.listen(source)
        try:
            command = listener.recognize_google(audio)
            command = command.lower()
            print("You:", command)
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that.")
            return ""
    return command

def run_assistant():
    speak("Hello, I am your voice assistant. How can I help you today?")
    while True:
        command = take_command()

        if 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            speak(f"The current time is {time}")

        elif 'date' in command:
            date = datetime.datetime.now().strftime('%B %d, %Y')
            speak(f"Today's date is {date}")

        elif 'wikipedia' in command:
            speak("What should I search on Wikipedia?")
            topic = take_command()
            try:
                info = wikipedia.summary(topic, sentences=2)
                speak(info)
            except:
                speak("Sorry, I couldn't find anything on Wikipedia.")

        elif 'search' in command:
            speak("What should I search on Google?")
            search_query = take_command()
            webbrowser.open(f"https://www.google.com/search?q={search_query}")
            speak(f"Here are the search results for {search_query}")

        elif 'youtube' in command:
            webbrowser.open("https://www.youtube.com")
            speak("Opening YouTube")

        elif 'gmail' in command:
            webbrowser.open("https://mail.google.com")
            speak("Opening Gmail")

        elif 'stop' in command or 'exit' in command or 'bye' in command:
            speak("Goodbye!")
            break

        elif command == "":
            continue
        else:
            speak("Sorry, I don't understand that command.")

run_assistant()