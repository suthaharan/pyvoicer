import gtts  
import os
from playsound import playsound  

# Base setup
file = open("draft.txt", "r",encoding="utf8").read().replace("\n", " ")

# make a request to google to get synthesis 
speech = gtts.gTTS(text = str(file), slow = False)

# save the audio file  
speech.save("draft.mp3")   

# play the audio file  
playsound("draft.mp3")  

#os.system("start draft.mp3")