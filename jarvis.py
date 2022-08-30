import pyttsx3
import speech_recognition as sr
import datetime 
import wikipedia
import webbrowser
import os 


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[0].id)

def speak(audio): 
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    elif hour>=18 and hour<21:
        speak("Good Evening")
    else:
        speak("Good Night")
    
    speak("I am Jarvis Sir. Always Ready for Your Command")

def takecommand():
    #it takes microphone input from the user and return string output

    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recognising...")
        query = r.recognize_google(audio,language='en-in')
        print(f"User said : {query}\n")

    except Exception as e:
        #print(e)

        print("Sorry sir I cant get u,please say that again")
        return "None"
    return query




if __name__=="__main__":
    wishMe()
    while True:
        query = takecommand().lower()

        #logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('searching WIKI..')
            quer=query.replace("wikipedia","")
            results= wikipedia.summary(query,sentences=1)
            speak("Acoording to WIKI")
            print(results)
            speak(results)
        if 'quit' in query:
            exit()
            speak('quitting sir. Thanks for your time')
        elif 'open youtube' in query:
            webbrowser.open('youtube.com')
        elif 'open google' in query:
            webbrowser.open('google.com')
        elif 'open stackoverflow' in query:
            webbrowser.open('stackoverflow.com')

        elif 'playmusic' in query:
            music_dir='C:\\Users\\DELL\\Music\\mysongs'
            songs= os.startfile(music_dir)
            print(songs)

        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M,%S")
            speak(f"the time is about{strTime}acoording to indian standard time")
        
        elif 'open code' in query:
            codepath ="C:\\Users\\DELL\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)

        
                
                
            


