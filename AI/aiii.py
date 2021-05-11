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
            audio=robot_ear.record(mic,duration=5)
        print("robot...")
        try:
            you=robot_ear.recognize_google(audio)

        except ValueError:
            you=''

        print("you:",you)

        if 'HI' in you:
            robot_brain="HELLO"
        elif 'WHAT IS YOUR NAME' in you:
            robot_brain="I am Jensen"
        elif 'HOW OLD ARE YOU' in you:
            robot_brain='I am 19'
        elif 'TODAY' in you:
            today=date.today()
            robot_brain=today.strftime("%B %d,%Y")
        elif 'TIME' in you:
            now=datetime.now()
            robot_brain=now.strftime("%H hours %M minutes %S seconds")
        elif " MR" in you:
            robot_brain='WOW'
        elif "HANDSOME" in you:
            robot_brain="yes yes yes"
        elif "BYE" in you:
            robot_brain="Goodbye"
            print("Robot:", robot_brain)
            robot_mouth.say(robot_brain)
            robot_mouth.runAndWait()
            break
        elif you=='':
            break
        elif you=='FUCK YOU':
            robot_brain="fuck you too ,ok :))"

        try:
            print("Robot:", robot_brain)
        except ValueError:
            exit()
        robot_mouth.say(robot_brain)
        robot_mouth.runAndWait()
