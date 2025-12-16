import pyttsx3

def generate_voice(text, output):
    engine = pyttsx3.init()
    engine.setProperty("rate", 175)
    engine.save_to_file(text, output)
    engine.runAndWait()
