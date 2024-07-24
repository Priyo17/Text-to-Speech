from gtts import gTTS
import os
mytext = 'welcome u all, im priyanka from 3rd year Cse C section studying at panimalar engineering college'
language = 'en'
myobj = gTTS(text=mytext, lang=language, slow=False)
myobj.save("welcome.mp3")
os.system("start welcome.mp3")


