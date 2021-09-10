import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import playsound
import wikipedia
import webbrowser
import os
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning")
    elif hour>=12 and hour<=18:
        speak("Good afternoon")
    else:
        speak("Good Evening")

    speak("Hello there! I am your assistant, how may i help you sir")

def inputcommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak Now I am Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognising Command..")
        query = r.recognize_google(audio, language= 'en-in')
        print(f"The user said {query}\n")
    except Exception as e:
        print(e)
        print("Pardon Pls..")
        return "None"
    return query


if __name__ == "__main__":
    wishme()
    # speak("Start speaking")
    # inputcommand()
    while True:
        query = inputcommand().lower()
        #logic for executing tasks based on query
        if 'wikipedia' in query:
            speak("Searching Wikipedia")
            query = query.replace("wikipedia", "")          #replace the word wikipedia in query
            results = wikipedia.summary(query, sentences = 2)   #this will store the 2 sentence summary of query in 
            speak("According to the Wikipedia")
            # print(results)
            speak(results)
            
            

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")  

        elif 'play music' in query:
            music_dir = 'E:\\Manas\\Dekstop\\SONGS\\eng songs'
            SONGS = os.listdir(music_dir)
               
            os.startfile(os.path.join(music_dir, SONGS[0]))