import pyttsx3
import threading

def speak_function(text):
    try:
        engine = pyttsx3.init()
        engine.setProperty('rate', 150)
        engine.say(text)
        engine.runAndWait()
        engine.stop()
    except:
        pass

def speak(text):
    # daemon=True завершує потік автоматично
    threading.Thread(target=speak_function, args=(text,), daemon=True).start()