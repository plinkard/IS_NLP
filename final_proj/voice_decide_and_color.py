import random
import time
from unicornhatmini import UnicornHATMini
import nltk
from textblob import TextBlob
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from gpiozero import Button
from signal import pause
import random
import time
import speech_recognition as sr

#nltk.download('vader_lexicon')

r=sr.Recognizer()

mic = sr.Microphone()

analyzer= SentimentIntensityAnalyzer()

uh = UnicornHATMini()



uh.set_brightness(0.15)


set = 0
running = True
go=False

def __color_set__():
    if set==0: #waiting
        for x in range(17):
            for y in range(7):
                uh.set_pixel(x, y, 100, 100, 100)
                uh.show()
    elif set==1: #neu
            for x in range(17):
                for y in range(7):
                    uh.set_pixel(x, y, 0, 0, 255)
                    uh.show()
    elif set==2: #pos
            for x in range(17):
                for y in range(7):
                    uh.set_pixel(x, y, 0, 255, 0)
                    uh.show()
    elif set==3: #neg
            for x in range(17):
                for y in range(7):
                    uh.set_pixel(x, y, 255, 0, 0)
                    uh.show()

def __getAudio__():
    with mic as source:
        r.adjust_for_ambient_noise(source)
        audio=r.listen(source)
    return r.recognize_google(audio)

def pressed(button):
    global go
    button_name = button_map[button.pin.number]
    if button_name == "A":
        go = True

button_map = {5: "A",
              6: "B",
              16: "X",
              24: "Y"}

button_a = Button(5)
button_b = Button(6)
button_x = Button(16)
button_y = Button(24)


swt=0
while running:
    set = 0

    if go:
        set=0
        __color_set__()
        sentence = __getAudio__()
        scored = analyzer.polarity_scores(sentence)['compound']

        if scored >= 0.2:
            set=2
            __color_set__()
            time.sleep(7)
            go = False

        elif scored<=-0.2:
            set=3
            __color_set__()
            time.sleep(7)
            go = False

        else:
            set=1
            __color_set__()
            time.sleep(7)
            go = False


    try:
        button_a.when_pressed = pressed
        button_b.when_pressed = pressed
        button_x.when_pressed = pressed
        button_y.when_pressed = pressed



    except KeyboardInterrupt:
        button_a.close()
        button_b.close()
        button_x.close()
        button_y.close()
