import pytesseract # install it using pip or pip3
import pyttsx3 # install it using pip or pip3

try:
    from PIL import Image
except ImportError:
    import Image

file1 = 'test.png'
file2 = 'w2.jpeg'
file3 = 'w1.jpeg'

document = pytesseract.image_to_string(Image.open(file2))


engine = pyttsx3.init() # object creation
engine.setProperty('rate', 500) # set the speecch rate

engine.say("Hello, Micheal! I am going to read you for this document.")
# print the document
print(document)
# read the document, text-to-speech
engine.say(document)
# run the engine 
engine.runAndWait()
# stop the engine
engine.stop()
