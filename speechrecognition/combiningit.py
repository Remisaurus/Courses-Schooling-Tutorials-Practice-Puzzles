import pyttsx3
import speech_recognition 

recognize = speech_recognition.Recognizer()
mic = speech_recognition.Microphone()
say = pyttsx3.init()

def sayit(text):
    voice = say.getProperty('voices') #get the available voices
    # say.setProperty('voice', voice[0].id) #set the voice to index 0 for male voice
    say.setProperty('voice', voice[2].id) #changing voice to index 2 for female voice (changes with available voices)
    say.say(text)
    say.runAndWait()
    
def listen():
    with mic as source:
        recognize.adjust_for_ambient_noise(source)
        audio = recognize.listen(source)
    return audio
    
def respond():
    try:
        this = recognize.recognize_google(listen())
        sayit(f'I think you said: {this}')
        if this == 'quit' or 'exit':
            quit()
    except speech_recognition.RequestError:
        sayit('I was unable to reach or get a response from the microphone')
    except speech_recognition.UnknownValueError:
        sayit('I did not understand, please try again.')
        respond()
        
respond()