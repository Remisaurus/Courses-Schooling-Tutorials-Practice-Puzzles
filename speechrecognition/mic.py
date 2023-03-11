# write: 'python -m speech_recognition' in console to check.

# microphone class:

import speech_recognition as sr


r = sr.Recognizer()

mic = sr.Microphone()

# print(sr.Microphone.list_microphone_names()) to see list if you want to use other than default,
# # This is just an example do not run; mic = sr.Microphone(device_index=3) will be 4th mic in list.

'''
just like the AudioFile class, Microphone is a context manager.
You can capture input from the microphone using the
listen() method of the Recognizer classinside of the with block.
This method takes an audio source as its first argument and records input from the source
until silence is detected.
'''

with mic as source:
    # r.adjust_for_ambient_noise(source)
    audio = r.listen(source)
    
# to recognize:
    
print(r.recognize_google(audio))    

'''
Audio that cannot be matched to text by the API raises an UnknownValueError exception.
You should always wrap calls to the API with try and except blocks to handle this exception.
'''


