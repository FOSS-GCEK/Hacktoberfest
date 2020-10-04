# Coded By-@YashNagare

# This module is imported so that we can  
# play the converted audio 
from gtts import gTTS
import os

# This will take file as an input
fr=open('sample.txt')

# reads data from file and stores in x
x=fr.read()

# Language in which you want to convert 
language='en'

# We need to pass text and language to the engine
# Here we have marked slow=False. Which tells us 
# the speed of audio should be fast
# gTTS library will convert this input into speech
audio=gTTS(text=x,lang=language,slow=False)

# Saving the converted audio in a .mp3 file
audio.save("sample.mp3")
os.system("sample.mp3")