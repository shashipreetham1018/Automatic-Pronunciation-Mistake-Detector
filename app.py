
from flask import Flask, render_template, request, jsonify
import pyttsx3
import speech_recognition as sr

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/check", methods=["POST"])
def check_pronunciation():
    target_word = request.form["target_word"]
    response = {"message": "", "status": ""}
    
    def listen():
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)
            try:
                return recognizer.recognize_google(audio)
            except sr.UnknownValueError:
                return ""
            except sr.RequestError:
                return ""

    def speak(text):
        engine = pyttsx3.init()
        engine.setProperty("rate", 150)
        engine.setProperty("volume", 1.0)
        engine.say(text)
        engine.runAndWait()

    speak(f"Please pronounce the word {target_word}")
    spoken_text = listen()

    if spoken_text.lower() == target_word.lower():
        response["message"] = "Correct pronunciation!"
        response["status"] = "success"
    else:
        response["message"] = "Incorrect pronunciation. Try again."
        response["status"] = "error"
    
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)
