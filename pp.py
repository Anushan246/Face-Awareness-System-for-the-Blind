import cv2
import pyttsx3
import threading
import time
from tkinter import Tk, Label, Entry, Button, StringVar

# Initialize the face cascade and text-to-speech engine
faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
engine = pyttsx3.init()

# Variables to store registered username and password
registered_username = None
registered_password = None

def speak_async(text):
    threading.Thread(target=speak, args=(text,)).start()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def voice_input(prompt):
    import speech_recognition as sr
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak(prompt)
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            speak(f"You said: {text}. Is this correct?")
            confirmation = input("Type 'yes' to confirm or 'no' to try again: ")
            if confirmation.lower() == 'yes':
                return text
            else:
                return voice_input(prompt)
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that. Please try again.")
            return voice_input(prompt)

def register():
    global registered_username, registered_password
    registered_username = username_var.get()
    registered_password = password_var.get()
    speak("Registration Successful!")
    register_window.destroy()
    start_face_detection()

def start_face_detection():
    speak("Starting face detection. Press Q to quit.")
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    cap.set(cv2.CAP_PROP_FPS, 10)

    prev_faces = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        small_frame = cv2.resize(frame, (640, 480))
        gray = cv2.cvtColor(small_frame, cv2.COLOR_BGR2GRAY)

        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30)
        )

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        cv2.imshow("Face Detection", frame)

        num_faces = len(faces)
        if num_faces != prev_faces:
            if num_faces == 0:
                speak_async("No faces detected!")
            elif num_faces == 1:
                speak_async("One face detected!")
            else:
                speak_async(f"{num_faces} faces detected!")

            prev_faces = num_faces

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        time.sleep(0.1)

    cap.release()
    cv2.destroyAllWindows()

def create_register_window():
    global register_window, username_var, password_var

    register_window = Tk()
    register_window.title("Register")

    username_var = StringVar()
    password_var = StringVar()

    speak("Welcome to the registration page.")

    username_label = Label(register_window, text="Username")
    username_label.grid(row=0, column=0)
    username_entry = Entry(register_window, textvariable=username_var)
    username_entry.grid(row=0, column=1)
    username_entry.bind("<FocusIn>", lambda e: speak("Enter username"))

    password_label = Label(register_window, text="Password")
    password_label.grid(row=1, column=0)
    password_entry = Entry(register_window, textvariable=password_var, show='*')
    password_entry.grid(row=1, column=1)
    password_entry.bind("<FocusIn>", lambda e: speak("Enter password"))

    register_button = Button(register_window, text="Register", command=register)
    register_button.grid(row=2, column=0, columnspan=2)
    register_button.bind("<FocusIn>", lambda e: speak("Press Enter to register"))

    voice_button = Button(register_window, text="Use Voice Input", command=lambda: use_voice_input())
    voice_button.grid(row=3, column=0, columnspan=2)
    voice_button.bind("<FocusIn>", lambda e: speak("Press Enter to use voice input"))

    speak("Use Tab to navigate between fields. Press Enter to activate buttons.")
    register_window.mainloop()

def use_voice_input():
    username = voice_input("Please say your username")
    username_var.set(username)
    password = voice_input("Please say your password")
    password_var.set(password)

if __name__ == '__main__':
    create_register_window()