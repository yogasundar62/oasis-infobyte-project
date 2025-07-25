import speech_recognition as sr
import pyttsx3
import datetime
import time
import webbrowser
def speak(text):
    engine = pyttsx3.init(driverName='sapi5')
    engine.setProperty('rate', 150)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()
def wish_user():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am your voice assistant. How can I help you today?")
def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio)
        print("You said:", query)
        return query.lower()
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that.")
        return ""
    except sr.RequestError:
        speak("Speech recognition service is not available.")
        return ""
def run_assistant():
    wish_user()
    while True:
        query = take_command()
        if "time" in query:
            current_time = time.strftime("%I:%M %p")
            speak(f"The current time is {current_time}")
        elif "date" in query:
            today = datetime.date.today()
            speak(f"Today's date is {today.strftime('%B %d, %Y')}")
        elif "search youtube for" in query:
            search_term = query.replace("search youtube for", "").strip()
            speak(f"Searching YouTube for {search_term}")
            webbrowser.open(f"https://www.youtube.com/results?search_query={search_term}")
        elif "search for" in query:
            search_term = query.replace("search for", "").strip()
            speak(f"Searching Google for {search_term}")
            webbrowser.open(f"https://www.google.com/search?q={search_term}")
        elif "exit" in query or "stop" in query or "bye" in query:
            speak("Goodbye! Have a great day.")
            break
        elif query:
            speak("Sorry, I don't understand that command yet.")
run_assistant()



