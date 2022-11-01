import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
import os
import pyautogui
import psutil
import pyjokes
import pywhatkit
import time
import sys
import random
from playsound import playsound

engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
newVoiceRate = 150
engine.setProperty("rate", newVoiceRate)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    

def ttime():
    Time = datetime.datetime.now().strftime("%I:%M %p")
    speak("the time is ")
    speak(Time)

def date():
    year = (datetime.datetime.now().year)
    month = (datetime.datetime.now().month)
    date = datetime.datetime.now().day
    
    speak("THE CURRENT DATE IS")
    speak(date)
    speak(month)
    speak(year)

def wish():
    speak("Welcome back Tharun!")
    hour = datetime.datetime.now().hour
    
    if hour >= 6 and hour < 12:
        speak("Happy Morning")
    elif hour >= 12 and hour < 16:
        speak("Good Afternoon")
    elif hour >=16 and hour <19:
        speak("Good Evening")
    elif hour >=19 and hour <22:
        speak("Its late evening !")
    else :
        speak("Its already late, go to bed")
    

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("I am listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        
    try:
        print("Recognising")
        query = r.recognize_google(audio)
        print(query)
        if 'alexa' in query:
            query = query.replace('alexa',"")
        print(query)
    except Exception as e:
        print(e)
        speak(e)
        return "NONE"
    return query

def sendmail(to,content):
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login("tharun.vnrkarthi@gmail.com","sribalaaji")
    server.sendmail("tharun.vnrkarthi@gmail.com",to,content)
    server.close()

def screenshot():
    img = pyautogui.screenshot()
    img.save("F:\ss\\1.png")
    
def cpu():
    usage = str(psutil.cpu_percent())
    speak("hmmmm....CPU is at "+ usage)
    
def jokes():
    speak(pyjokes.get_joke())
    
def quit():
    while True:
        runAlexa()
        break

def addgrocery():
    speak("What should i add?")
    data = takeCommand()
    speak ("Tharun, you said me to add " + data )
    grocery = open("grocery.txt","a")
    grocery.write("\n")
    grocery.write(data)
    grocery.close()

def grocerylist():
    remember = open("grocery.txt","r")
    speak("You said me to remember that" + remember.read())
    remember.close()
    
def deletegrocery():
    delete = open("grocery.txt","w")
    delete.write("")
    speak("Grocery list updated")
    delete.close()

def playsong():
    n = random.randint(0, 100)
    music_dir = "E:\\Songs\\08mid"
    song = os.listdir(music_dir)
    os.startfile(os.path.join(music_dir, song[n]))
    
def alarm():
    speak("feed the remainder details as text")
    speak("What is this Remainder for: ")
    details = takeCommand()
    speak("Enter the hour")
    hour = int(input("Enter Hour(1 to 12): "))
    speak("Enter the minute")
    minu = int(input("Enter minute: "))
    speak("Is it A M or P M")
    ttime  = input("AM/PM: ")
    speak("I will remaind you")
    if ttime == "pm":
            hour += 12
    while True:
        if hour == datetime.datetime.now().hour and minu == datetime.datetime.now().minute:
            print("I am Remainding")
            speak("I am Remainding ")
            speak(details)
            playsound("KaatrinmozhiBgm.mp3")
            break
 
    
    
def runAlexa():
    te = int(datetime.datetime.now().strftime("%H"))
    ts = int(datetime.datetime.now().strftime("%M"))
    ts1 = ts+1
    appa =' 91 9361381816'
    amma = '91 6380923193'
    thatha = '91 9444967878'
    bhama = '91 9344031768'
    
    
    query = takeCommand().lower()
        
    if "time" in query:
            ttime()
    elif "date" in query:
            date()
    elif "wikipedia" in query:
            speak("Searching")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query, sentences = 2)
            speak(result)
    elif "offline" in query:
            speak("Bye for now")
            sys.exit()
    elif "mail" in query:
            try:
                speak("What should i Convey?")
                content = takeCommand()
                to = "2032046mds@cit.edu.in"
                sendmail(to, content)
                speak("i sent it successfully")
            except Exception as e:
                speak(e)
                speak("Sorry! I was not able to send the mail")
    elif "chrome" in query:
            speak("i face some issues right now! Sorry")
            chromepath = "C:\ProgramFiles\Google\Chrome\Application\chrome.exe %s"
            search = takeCommand().lower()
            wb.get(chromepath).open_new_tab("https://" +search+ ".com")
    elif "logout" in query:
            os.system("shutdown - 1")
            
    elif "shutdown" in query:
            os.system("shutdown /s /t 1")
            
    elif "restart" in query:
            os.system("shutdown /r /t 1")

        
    elif "remember" in query:
            speak("What should i remember?")
            data = takeCommand()
            speak ("Tharun, you said me to remember" + data )
            remember = open("data.txt","w")
            remember.write(data)
            remember.close()
        
    elif "do you know anything" in query:
            remember = open("data.txt","r")
            speak("You said me to remember that" + remember.read())
            
    elif "screen grab" in query:
            screenshot()
            speak("ouch!!There is some error!")
            
    elif "health" in query:
            cpu()
            
    elif "madurai veeran things" in query:
            jokes()
            
    elif "play from web" in query:
            song = query.replace('play from web','')
            speak(' playing '+ song)
            pywhatkit.playonyt(song)
            speak("I am back")
            
    elif "thank you" in query:
            speak("its my pleasure helping you")
        
    elif "don't listen" in query or "stop listening" in query:
            speak("okay")
            time.sleep(1000)
            speak("I am back")
            
    elif "add to grocery list" in query:
            addgrocery()
           
    elif "show grocery list" in query:
            grocerylist()
            
    elif "delete grocery list" in query:
            deletegrocery()
            
    elif "play from machine" in query:
            speak("Sure! Finding best playlists for you")
            playsong()
            
    elif "what is your name" in query:
            speak("I am poooochu ! Your virtual voice assisstant")
            
    elif "whatsapp" in query:
            speak("Speak out the number")
            no = takeCommand().lower()
            if "appa" in no:
                no1 = appa
            elif "amma" in no:
                no1 = amma
            elif "thatha" in no:
                no1 = thatha
            elif "bhama" in no:
                no1 = bhama
            else:
                no1=no
            speak("What is the message")
            msg = takeCommand()
            pywhatkit.sendwhatmsg_instantly('+'+no1, msg)
            
    elif "reminder" in query:
            alarm()
    
    elif "group message" in query:
            speak("Send message to which group?")
            grpname = takeCommand()
            if "cit4" in grpname:
                grpid = 'IXX6MI5t9qo7tbobNKyL5p'
            
            speak("What should i convey")
            grpmsg = takeCommand()
            pywhatkit.sendwhatmsg_to_group(grpid,grpmsg,te,ts1)    

        
    else:
            speak("can you repeat that please")
            
            
if __name__ == "__main__":

    wish() 
    while True:
            runAlexa()

    

