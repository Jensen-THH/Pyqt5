from datetime import date,datetime
import speech_recognition
import pyttsx3
robot_mouth = pyttsx3.init()
robot_ear =speech_recognition.Recognizer()
robot_brain=""
while True:
        with speech_recognition.Microphone() as mic:
            robot_ear.adjust_for_ambient_noise(mic)
            print("Robot listening")
            audio=robot_ear.record(mic,duration=3)
            you=robot_ear.recognize_google(audio)
        print("robot...")
        try:
            you=robot_ear.recognize_google(audio)
        except(ValueError):
            you=''

        print("you:",you)


        if 'hi' in you:
            robot_brain="HELLO"
        elif 'what is your name'in you:
            robot_brain="I am Jensen"
        elif 'how old are you' in you:
            robot_brain='I am 19'
        elif 'today' in you:
            today=date.today()
            robot_brain=today.strftime("%B %d,%Y")
        elif 'time' in you:
            now=datetime.now()
            robot_brain=now.strftime("%H hours %M minutes %S seconds")
        elif "mr" in you:
            robot_brain='xin chao mrs Tinh'
        elif "handsome" in you:
            robot_brain="yes yes yes"
        elif "bye" in you:
            robot_brain="Goodbye"
            print("Robot:", robot_brain)
            robot_mouth.say(robot_brain)
            robot_mouth.runAndWait()
            break
        elif you=='':
            break
        elif you=='fuck you':
            robot_brain="fuck you too ,ok :))"
        #else:
           # robot_brain=you
            #robot_brain="I can't hear you"
        print("Robot:",robot_brain)
        robot_mouth.say(robot_brain)
        robot_mouth.runAndWait()
