import pyttsx3
import datetime
import webbrowser
import os
import wikipedia
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>0 and hour<12:
        speak("Good morning")
    elif hour>12 and hour<18:
        speak("Good afternoon")
    else:
        speak("Good evening")
    speak("I am Nikki, How can i help you")

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
    # print(e)    
        print("Say that again please...")  
        return "None"
    return query


if __name__ == "__main__":
    wishme()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   


        elif 'play music' in query:
            music_dir = 'C:/Users/HKC/Desktop/song new'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))
        elif 'open notes' in query:
            document_dir = 'C:/Users/HKC/Desktop/notes'
            documents = os.listdir(document_dir)    
            os.startfile(os.path.join(document_dir, documents[0]))


        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"the time is {strTime}")
            print(strTime)

        elif 'hello' in query:
            speak("Hello! How are you")
            print(speak)

        elif 'how are you' in query:
            speak("I am doing great! Thankyou")
            print(speak)

        elif 'Thankyou' in query:
            speak("Happy to help you")
           
        

