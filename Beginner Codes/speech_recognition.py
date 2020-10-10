import speech_recognition as srg
import time
store = srg.Recognizer()
with srg.Microphone() as s:
    print("Speak...")
    audio = store.record(s,duration=7)
    print("Recording time:",time.strftime("%I:%M:%S"))
    print("Recorded")
    try:
        output = store.recognize_google(audio)
        print(output)
        print("Executing time:",time.strftime("%I:%M:%S"))
    except:
        print("not working")