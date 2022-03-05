import speech_recognition

def Listen():
    recognizer = speech_recognition.Recognizer()

    with speech_recognition.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        return command

    except KeyboardInterrupt:
        print("Process interrupted")
        return None

    except speech_recognition.RequestError as e:
        print("Could not request results: {0}".format(e))
        return None

    except speech_recognition.UnknownValueError:
        print("Unknown Error Occured")
        return None
