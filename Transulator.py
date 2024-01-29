import tkinter as tk
from tkinter import ttk
import threading
import requests
import speech_recognition as sr
from gtts import gTTS
import playsound
import os

# Initialize recognizer and microphone
r = sr.Recognizer()
stop_listening = False

def recognize_speech(language):
    global stop_listening
    with sr.Microphone() as source:
        # Adjust for ambient noise to reduce background noise
        r.adjust_for_ambient_noise(source, duration=1)
        status_label.config(text=f"Please speak something in {language}...")
        root.update()
        audio = r.listen(source)

        if stop_listening:
            return None

    try:
        # Recognize speech using the specified input language
        user_speech = r.recognize_google(audio, language=language)
        status_label.config(text=f"You said ({language}): {user_speech}")
        root.update()
        return user_speech

    except sr.UnknownValueError:
        status_label.config(text="Could not understand audio")
        root.update()
        return None

def translate_and_speak():
    global stop_listening
    current_language = passenger_language.get()
    switch_button.config(state=tk.DISABLED)
    stop_button.config(state=tk.NORMAL)
    
    while True:
        if current_language == passenger_language.get():
            status_label.config(text="Switched to Passenger's language.")
        else:
            status_label.config(text="Switched to Employee's language.")
        
        user_speech = recognize_speech(current_language)

        if user_speech:
            target_language = employee_language.get() if current_language == passenger_language.get() else passenger_language.get()
            translated_text = translate_text(user_speech, current_language, target_language)
            status_label.config(text=f"Translated text: {translated_text}")
            speak_text(translated_text, target_language)
        
        current_language = passenger_language.get() if current_language == employee_language.get() else employee_language.get()
        root.update()

def start_translation_thread():
    global stop_listening
    stop_listening = False
    translation_thread = threading.Thread(target=translate_and_speak)
    translation_thread.daemon = True
    translation_thread.start()
    switch_button.config(state=tk.DISABLED)
    stop_button.config(state=tk.NORMAL)

def stop_listening_thread():
    global stop_listening
    stop_listening = True
    switch_button.config(state=tk.NORMAL)
    stop_button.config(state=tk.DISABLED)

def translate_text(text, source_language, target_language):
    base_url = "https://translate.googleapis.com/translate_a/single"
    params = {
        "client": "gtx",
        "sl": source_language,
        "tl": target_language,
        "dt": "t",
        "q": text,
    }

    response = requests.get(base_url, params=params)
    translation = response.json()[0][0][0]
    return translation

def speak_text(text, language):
    tts = gTTS(text=text, lang=language)
    tts.save("output.mp3")  # Save the speech to a file
    playsound.playsound("output.mp3")  # Play the saved speech
    # Remove the temporary file
    os.remove("output.mp3")

root = tk.Tk()
root.title("Language Translator")

passenger_language_label = ttk.Label(root, text="Passenger's Language:")
passenger_language_label.grid(row=0, column=0)
passenger_language = tk.StringVar()
passenger_language_entry = ttk.Entry(root, textvariable=passenger_language)
passenger_language_entry.grid(row=0, column=1)

employee_language_label = ttk.Label(root, text="Employee's Language:")
employee_language_label.grid(row=1, column=0)
employee_language = tk.StringVar()
employee_language_entry = ttk.Entry(root, textvariable=employee_language)
employee_language_entry.grid(row=1, column=1)

status_label = ttk.Label(root, text="Status: Waiting for input...")
status_label.grid(row=2, column=0, columnspan=2)

switch_button = ttk.Button(root, text="Start Translation", command=start_translation_thread)
switch_button.grid(row=3, column=0)
stop_button = ttk.Button(root, text="Stop Listening", command=stop_listening_thread, state=tk.DISABLED)
stop_button.grid(row=3, column=1)

root.mainloop()
