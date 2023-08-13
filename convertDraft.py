import gtts  
import os
from playsound import playsound  

# Base setup
file = open("draft-ta.txt", "r",encoding="utf8").read().replace("\n", " ")
language = 'ta'

# make a request to google to get synthesis 
speech = gtts.gTTS(text = str(file), lang = language, slow = False)

# save the audio file  
speech.save("draft.mp3")   

# play the audio file  
playsound("draft.mp3")  

#os.system("start draft.mp3")