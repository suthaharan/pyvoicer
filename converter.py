import gtts  
from playsound import playsound  

# make a request to google to get synthesis  
t1 = gtts.gTTS("Welcome to javaTpoint Swaminathan")  

# save the audio file  
t1.save("welcome.mp3")   

# play the audio file  
playsound("welcome.mp3")  