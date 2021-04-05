import pyttsx3
import speech_recognition as sr
import pyaudio
import datetime

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice' , voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning!")
    elif hour>=12 and hour<18:
        speak("good afternoon!")
    else:
        speak("good evening!")
    speak("I am jarvis sir. please tell me may i help you")



def takeCommand():
    #it takes microphone input from the user and returns string input

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said:{query}\n")

    except Exception as e:
        #print(e)
        print("samj mai nhi aya ...")
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    takeCommand()


    def reverseList(A, start, end):
        while start < end:
            A[start], A[end] = A[end], A[start]
            start += 1
            end -= 1


    A = [1, 2, 3, 4, 5, 6]
    print(A)
    reverseList(A, 0, 5)
    print("Max no is ")
    print(A)

    import speech_recognition as sr
    import pyaudio


def takeCommand():
    #it takes microphone input from the user and returns string input

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said:{query}\n")

    except Exception as e:
        #print(e)
        print("say that again...")
        return "None"
    return query
