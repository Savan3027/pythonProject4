import pyttsx3

if __name__ == '__main__':
    engine = pyttsx3.init()
    while True:
        X = input("Enter what you want me to pronounce: ")
        if X == "q":
            engine.say('bye bye friend')
            engine.runAndWait()
            break
        engine.say(X)
        engine.runAndWait()