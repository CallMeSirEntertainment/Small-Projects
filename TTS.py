import pyttsx3
first = True
while True:
    engine = pyttsx3.init()
    if first is True:
        first = False
        text = input("Enter the text to convert to speech.\n")
    else:
        text = input("\nEnter the text to convert to speech.\n")
    engine.say(text)
    engine.runAndWait()