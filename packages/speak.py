import pyttsx3

def Speak(command):
    engine = pyttsx3.init()
    engine.setProperty('rate', 120)
    engine.setProperty('volume', 1)
    engine.say(command)
    print(command)
    engine.runAndWait()
