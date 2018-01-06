import speech_recognition as sr
from gtts import gTTS
import os


# get audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Speak:")
    audio = r.listen(source)
mytext=r.recognize_google(audio)

try:
    print("You said " + r.recognize_google(audio))
except sr.UnknownValueError:
    print("Could not understand audio")
except sr.RequestError as e:
    print("Could not request results; {0}".format(e))
# The text that you want to convert to audio

# Language in which you want to convert
language = 'en'

# Passing the text and language to the engine,
# here we have marked slow=False. Which tells
# the module that the converted audio should
# have a high speed
myobj = gTTS(text=mytext, lang=language, slow=False)

# Saving the converted audio in a mp3 file named
# welcome
myobj.save("welcome.mp3")

# Playing the converted file
os.system("start welcome.mp3")
