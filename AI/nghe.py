import speech_recognition
robot_ear =speech_recognition.Recognizer()
with speech_recognition.Microphone() as mic:
    print("Robot listening")
    print("robot...")
    audio=robot_ear.record(mic,duration=3)

try:
    you=robot_ear.recognize_google(audio)
except:
    you==""
print("you:"+you)
