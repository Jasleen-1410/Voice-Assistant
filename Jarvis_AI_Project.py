# # import cv2
# import pyttsx3
# import speech_recognition as sr
# import datetime
# import wikipedia
# import webbrowser
# import os
# import keyboard
# import sys

# print("Jiya maa")

# # alias python="python3"


import pyttsx3                                         # Text to speech library
import speech_recognition as sr                        # Speech Recongnition 
import datetime                                        # Date and time library 
import wikipedia                                       # To access and parse data from Wikipedia
import webbrowser                                      # To access web browser
import os                                              # For interacting with the operating system
import keyboard                                        # To interact with the keys pressed by keyboard
import sys                                             # To interact with the system


# Sets the engine to get the voice
engine = pyttsx3.init()
voices = engine.getProperty('voices')                 # Getting details of current voice
# print(voices[1].id)
engine.setProperty('voice',voices[0].id)              # voice id helps us to select different voices [0] for male, [1] for female


# Convert text to speech
def speak(audio):  
    engine.say(audio)
    engine.runAndWait()                                # Without this command, speech will not be audible to us.


# Ask name function
def askname():
    name = input("Kindly enter your name....")
    keyboard.wait('enter')

    speak(f"{name}, such a nice name")
    speak(f"How can I help you {name}, let me know, I am there for your service")

    

# If user enters y then program continues else it ends
def keypressed():
    key = keyboard.read_key()

    if keyboard.is_pressed('y'):  
            print(f'You Pressed {key} Key! \nHey there! My name is Jarvis. What is your name?')
            speak(f'You Pressed {key} Key! \nHey there! My name is Jarvis. What is your name?')
            askname()
    elif keyboard.is_pressed(key):  
            print(f'You Pressed {key} Key! \nThanks for coming :)')
            speak(f'You Pressed {key} Key! \nThanks for coming :)')
            sys.exit(0)
            


# Jarvis will greet me according to the time 
def wishMe():
    hour = int(datetime.datetime.now().hour)           #stored the integer value of the current hour 
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Jarvis. Press Y if you want to continue else Press ENTER or any other key if you want to quit......")
    print("I am Jarvis. Press 'Y' if you want to continue else Press ENTER or any other key if you want to quit......")
    #keypressed()





# take command with the help of the microphone of the user's system
# It takes microphone input from the user and returns string output
def takeCommand():
    if keyboard.is_pressed('enter') or keyboard.is_pressed('q'):  # if key 'enter' or 'q' is pressed 
            print('You quited the program! My service ends here! Thanks for coming.')
            speak('You quited the program! My service ends here! Thanks for coming.')
            sys.exit(0)

    r = sr.Recognizer()
    with sr.Microphone() as source:                                   # use the default microphone as the audio source
        print("\nListening...")
        r.pause_threshold = 1 
        audio = r.listen(source)                                      # listen for the first phrase and extract it into audio data
    
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')           #Using google for voice recognition.
        print(f"You said: {query}\n")                                 #User query will be printed.

    except Exception as e:
        print(e)    
        print("Can't understand ! Say that again please...")          #Say that again will be printed in case of improper voice 
        speak("Can't understand ! Say that again please...") 
        return "None"                                                 #None string will be returned
    return query

    


# Creating Our main() functionS
# __name__ is a built-in variable which evaluates to the name of the current module
# If the source file is executed as the main program, the interpreter sets the __name__ variable to have a value “__main__”
if __name__=="__main__" :
    speak("\a Welcome to Jarvis world")
    wishMe()
    while True: 
            query=takeCommand().lower()                  # Converting user query into lower case
            
            # Task 1
            if 'name' in query:
                speak("My name is Jarvis. What is your good name?")
                name= takeCommand().lower()
                speak(f"{name} such a sweet name! ")     # The letter “f” also indicates that these strings are used for formatting.


            # Task 2
            elif 'open youtube' in query:
                webbrowser.open("youtube.com")
                speak("Opening Youtube!")

            # Task 3
            elif 'open google' in query:
                webbrowser.open("google.com")
                speak("Opening google in Microsoft edge broswer!")
            
            # Task 4
            elif 'wikipedia' in query:                   # If wikipedia found in the query then this block will be executed
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia of ", "")
                results = wikipedia.summary(query, sentences=3) 
                speak("According to Wikipedia: ")
                print(results)
                speak(results)
    
            # Task 5
            elif 'the time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")   
                speak(f"The current time is {strTime}")
            
            # Task 6
            elif 'date' in query:  
                strDate = datetime.datetime.now().strftime("%d:%m:%Y")
                speak(f"Today's date is {strDate}")

            # Exiting the loop
            elif 'bye' in query:
                speak("Bye, It was really nice meeting you. Have a Good day!")
                break

        
