
from unicodedata import category
import pyttsx3 
import speech_recognition as sr
import webbrowser 
import datetime
import pyjokes
import os
import time

def sptext():
    recognizer=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("recognizing...")
            data=recognizer.recognize_google(audio)
            print(data)
            return data
        except sr.UnknownValueError:
            print("Not Understand")

def speechtx(x):
    engine = pyttsx3.init()
    voices =engine.getProperty("voices")
    engine.setProperty("voice",voices[1].id)
    rate = engine.getProperty("rate")
    engine.setProperty("rate",150)
    engine.say(x)
    engine.runAndWait()

if __name__ == "__main__":

    if "hello" in sptext().lower():
        while True:
            data1=sptext().lower()

            if "your name" in data1:
                name = "my name is peter"
                speechtx(name)

            elif "old are you" in data1:
                age = " abhi abhi to paida hua hu mai"
                speechtx(age)

            elif "time" in data1:
                time1 = datetime.datetime.now().strftime("%I%M%p")
                speechtx(time1)
            
            elif "youtube" in data1:
                webbrowser.open("https://www.youtube.com")
            
            elif "web" in data1:
                webbrowser.open("https://www.google.com")

            elif "joke" in data1:
                joke_1=pyjokes.get_joke(language="en",category="neutral")
                print(joke_1)
                speechtx(joke_1)

            elif "play a song" in data1:
                add= "D:\song"
                listsong = os.listdir(add)
                print(listsong)
                os.startfile(os.path.join(add,listsong[1]))
            
            elif "exit" in data1:
                speechtx("thank you")
                break 
            time.sleep(5)

else:
    print("thanks")



