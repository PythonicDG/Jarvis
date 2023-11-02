from types import coroutine
import pyttsx3
import speech_recognition as sr
from feature import GoogleSearch
from win10toast import ToastNotifier
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import sqlite3
import datetime
import pipwin


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[2].id)

con = sqlite3.connect('jarvis.db')
cursorObj = con.cursor()
# cursorObj.execute("CREATE TABLE IF NOT EXISTS audio(content TEXT)")
# con.commit()


def Speak(audio):
    print(" ")
    print(f": {audio}")
    engine.say(audio)
    engine.runAndWait()
    print(" ")

def TakeCommand():

    r = sr.Recognizer()

    with sr.Microphone() as source:

        print(": Listening....")
        Speak("Listening..")

        r.pause_threshold = 1

        audio = r.listen(source)

    try:

        print(": Recognizing...")
        Speak("Recognizing...")

        query = r.recognize_google(audio,language='en-in')

        print(f": Your Command : {query}\n")

    except:
        return ""
    # cursorObj.execute("INSERT INTO audio(content) VALUES(?)", (info,))
    # con.commit()
    return query.lower()

def TaskExe():

    while True:

        query = TakeCommand()

        if 'google search' in query:
            GoogleSearch(query)

        elif 'youtube search' in query:
            Query = query.replace("jarvis","")
            query = Query.replace("youtube search","")
            from feature import YouTubeSearch
            YouTubeSearch(query)

        elif 'set alarm' in query:
            from feature import Alarm
            Alarm(query)

        elif 'download' in query:
            from feature import DownloadYouTube
            DownloadYouTube()

        elif 'speed test' in query:
            from feature import SpeedTest
            SpeedTest()

        elif 'whatsapp message' in query:

            name = query.replace("whatsapp message","")
            name = name.replace("send ","")
            name = name.replace("to ","")
            Name = str(name)
            Speak(f"Whats The Message For {Name}")
            MSG = TakeCommand()
            from Automation import WhatsappMsg
            WhatsappMsg(Name,MSG)

        elif 'call' in query:
            from Automation import WhatsappCall
            name = query.replace("call ","")
            name = name.replace("jarvis ","")
            Name = str(name)
            WhatsappCall(Name)

        elif 'show chat' in query:
            Speak("With Whom ?")
            name = TakeCommand()
            from Automation import WhatsappChat
            WhatsappChat(name)

        elif 'space news' in query:


            Speak("Tell Me The Date For News Extracting Process .")

            Date = TakeCommand()

            from feature import DateConverter

            Value = DateConverter(Date)

            from nasa import NasaNews

            NasaNews(Value)

        elif 'about' in query:
            from nasa import Summary
            query = query.replace("jarvis ","")
            query = query.replace("about ","")
            Summary(query)

        elif 'mars images' in query:

            from nasa import MarsImage

            MarsImage()

        elif 'track iss' in query:

            from nasa import IssTracker

            IssTracker()

        elif 'near earth' in query:
            from nasa import Astro
            from feature import DateConverter
            Speak("Tell Me The Starting Date .")
            start = TakeCommand()
            start_date = DateConverter(TakeCommand)
            Speak("And Tell Me The End Date .")
            end = TakeCommand()
            end_date = DateConverter(end)
            Astro(start_date,end_date=end_date)

        elif 'my location' in query:

            from feature import My_Location

            My_Location()

        elif 'where is' in query:

            from Automation import GoogleMaps
            Place = query.replace("where is ","")
            Place = Place.replace("jarvis" , "")
            GoogleMaps(Place)

        elif 'online' in query:

            from Automation import OnlinClass

            Speak("Tell Me The Name Of The Class .")

            Class = TakeCommand()

            OnlinClass(Class)

        elif 'write a note' in query:

            from Automation import Notepad

            Notepad()

        elif 'dismiss' in query:

            from Automation import CloseNotepad

            CloseNotepad()

        elif 'time table' in query:

            from Automation import TimeTable

            TimeTable()

        elif 'activate the bulb' in query:

            from Database.HomeAuto.SmartBulb import Activate

            Activate()

            Speak("Should I Start Or Close The Bulb ?")

            step = TakeCommand()

            if 'close' in step:

                from Database.HomeAuto.SmartBulb import CloseLight

                CloseLight()

            elif 'start' in step:

                from Database.HomeAuto.SmartBulb import StartLight

                StartLight()

        elif 'corona cases' in query:

            from feature import CoronaVirus

            Speak("Which Country's Information ?")

            cccc = TakeCommand()

            CoronaVirus(cccc)

        else:

            from Database.ChatBot.ChatBot import ChatterBot

            reply = ChatterBot(query)

            Speak(reply)

            if 'bye' in query:

                break

            elif 'exit' in query:

                break

            elif 'go' in query:

                break
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        Speak("Good Morning!")
    elif hour>=12 and hour<18:
        Speak("Good Afternoon!")
    else:
        Speak("Good Evening!")

    Speak('Helloo, Please tell me how may I help you')
    TaskExe()
# cursorObj.close()
# con.close()
