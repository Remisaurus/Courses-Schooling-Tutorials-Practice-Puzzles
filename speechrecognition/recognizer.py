import speech_recognition as sr
print(sr.__version__)

r = sr.Recognizer()
'''
Each Recognizer instance has seven methods for recognizing speech from an audio source using various APIs. These are:

recognize_bing(): Microsoft Bing Speech
recognize_google(): Google Web Speech API
recognize_google_cloud(): Google Cloud Speech - requires installation of the google-cloud-speech package
recognize_houndify(): Houndify by SoundHound
recognize_ibm(): IBM Speech to Text
recognize_sphinx(): CMU Sphinx - requires installing PocketSphinx
recognize_wit(): Wit.ai

Of the seven, only recognize_sphinx() works offline with the CMU Sphinx engine.
The other six all require an internet connection.
'''

# r.recognize_google()

'''
SpeechRecognition makes working with audio files easy thanks to its handy AudioFile class.
This class can be initialized with the path to an audio file,
and provides a context manager interface for reading and working with the file’s contents.
'''

harvard = sr.AudioFile('harvard.wav')

with harvard as source:
    audio = r.record(source) # can add: ''',offset=2.2, duration=1.1''' between paranthesis

''' 
The context manager opens the file and reads its contents,
storing the data in an AudioFile instance called source.
Then the record() method records the data from the entire file into an AudioData instance. 
'''

print(type(audio))

'''
You can now invoke recognize_google() to attempt to recognize any speech in the audio.
Depending on your internet connection speed,
you may have to wait several seconds before seeing the result.
'''

print(r.recognize_google(audio))

'''
What if you only want to capture a portion of the speech in a file?
The record() method accepts a duration keyword argument
that stops the recording after a specified number of seconds.

In addition to specifying a recording duration,
the record() method can be given a specific starting point using the offset keyword argument.
This value represents the number of seconds from the beginning of the file
to ignore before starting to record.
'''

'''
Noise
using the adjust_for_ambient_noise() method of the Recognizer class.
'''

with harvard as source:
     r.adjust_for_ambient_noise(source)
     audio = r.record(source)

'''
You can adjust the time-frame that adjust_for_ambient_noise()
uses for analysis with the duration keyword argument.
This argument takes a numerical value in seconds and is set to 1 by default.
r.adjust_for_ambient_noise(source, duration=0.5)

always returns most likely unless you state otherwise.
r.recognize_google(audio, show_all=True)
'''


