# Python program to translate
# speech to text and text to speech


import speech_recognition as sr
import pyttsx3 

# Initialize the recognizer 
r = sr.Recognizer() 

# Function to convert text to
# speech
def SpeakText(command):
	
	# Initialize the engine
	engine = pyttsx3.init()
	engine.say(command) 
	engine.runAndWait()
	
	
# Loop infinitely for user to
# speak

temp = ""
file1 = open('dump.txt','w+')
while(1): 

    # Exception handling to handle
    # exceptions at the runtime
    try:

        # use the microphone as source for input.
        with sr.Microphone() as source2:

            # wait for a second to let the recognizer
            # adjust the energy threshold based on
            # the surrounding noise level 
            r.adjust_for_ambient_noise(source2, duration=0.2)

            #listens for the user's input 
            print("Listening for user's input:")
            audio2 = r.listen(source2)
        
        # sam = sr.AudioFile('sample4.wav')
        # with sam as source:
        #     print("Listening for audio: ")
        #     audio2 = r.record(source)
            # Using google to recognize audio
            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()

            if MyText.split()[-1] == "exit":
                print("Thank You, terminating")
                break

            # print("Did you say ",MyText)
            # SpeakText(MyText)
            temp += " "+MyText
        print("Listening Complete: Terminating")
        break
        
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

    except sr.UnknownValueError:
        print("unknown error occurred")

file1.write(temp)
file1.close()