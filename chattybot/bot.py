
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from cleaner import clean_corpus
from gtts import gTTS
import sounddevice as sd
import soundfile as sf
import speech_recognition

# with .clock error from sqlalchemy: replace the time.clock with time.perf_counter()

CORPUS_FILE = "./studydata/chat.txt"

language = 'nl'
chategg = ChatBot("Chategg")
trainer = ListTrainer(chategg)
recognize = speech_recognition.Recognizer()
mic = speech_recognition.Microphone()

exit_conditions = (":q", "quit", "exit", "stop")

def sayit(text):
    myobj = gTTS(text=text, lang=language, slow=False)
    myobj.save("Sayit.wav")
    data, fs = sf.read('Sayit.wav', dtype='float32')  
    sd.play(data, fs)
    status = sd.wait()  # Wait until file is done playing
    
def listen():
    with mic as source:
        recognize.adjust_for_ambient_noise(source)
        audio = recognize.listen(source, phrase_time_limit=5)
    return audio
    
def querying():
    try:
        this = recognize.recognize_google(listen(), language = 'nl-NL')
        return this
    except speech_recognition.RequestError:
        sayit('I was unable to reach or get a response from the microphone')
    except speech_recognition.UnknownValueError:
        return 'Niet verstaan'

def communicate():
    query = querying()
    print('user said: ' + query)
    if query in exit_conditions:
        quit()
    else:
        respons = chategg.get_response(query)
        print(f"🥚 {respons}")
        sayit(str(respons))
        communicate()

# starting chatbot (Dutch in this case)
    
sayit('Geef mij een paar minuten om gegevens te bestuderen.')
sayit('Ik ga nu beginnen.')

# teaching chatbot (with txt file exported with Whatsapp stated in CORPUS_FILE) 

cleaned_corpus = clean_corpus(CORPUS_FILE)

#trainer.train(cleaned_corpus)
trainer.train([
    "Hoi",
    "Hallo, vriend",
])
trainer.train([
    "ben jij een ei?",
    "Nee, ik zit in een ei",
])

#starting communication

sayit('Ok, ik ben er klaar voor. de regels zijn dat ik elke keer 1 seconde nodig heb nadat ik wat heb gezegt om de microfoon te calibreren, en dat je daarna 5 seconden hebt om wat te zeggen.')

communicate()




