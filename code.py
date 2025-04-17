import pyttsx3
import speech_recognition as sr
import webbrowser
import otp

def speak(text):
  engine = pyttsx3.init()
  voices = engine.getProperty('voices')
  engine.setProperty('voice',voices[1].id)
  engine.say(text)
  engine.runAndWait() 
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak to recognize.....")
        r.pause_threshold = 2
        audio = r.listen(source)
        try:
            print("Recognizing......")
            query = r.recognize_google(audio,language="en-in")
            print(query)
        except:
            print("Speak Again")
            return False
        else:
            return query
def greet():
    greeting = "Hello, How can i help You ?"
    speak(greeting)
greet()
while True:
    query = takecommand()
    if query == False:
        pass
    elif "how are you" in query.lower():
        speak("I am doing Good, How about you !")
    
    elif "open web page" in query.lower():
        speak("Opening google Website !")
        webbrowser.open("www.google.com")
    elif "send otp" in query.lower():
        speak("Enter Email address: ")
        x = input("Enter email here: ")
        otp.otp(x)
        speak("Otp Sent Sucessfully")
    elif "open linkedin" in query.lower():
        speak("Opening LinkedIn")
        webbrowser.open("https://www.linkedin.com")
    elif "open github" in query.lower():
        speak("Opening GitHub")
        webbrowser.open("https://www.github.com")
    elif "shut down" in query.lower():
        speak("Take Care, Bye !")
        break
