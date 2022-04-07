import random
import time
from unicornhatmini import UnicornHATMini
import nltk
from textblob import TextBlob
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from gpiozero import Button
from signal import pause

#nltk.download('vader_lexicon')


analyzer= SentimentIntensityAnalyzer()

uh = UnicornHATMini()

uh.set_brightness(0.5)


set = 0
running = True

def __color_set__():
    if set==0: #waiting
        for x in range(17):
            for y in range(7):
                uh.set_pixel(x, y, 255, 255, 0)
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

def pressed(button):
    button_name = button_map[button.pin.number]
    if button_name == "A":
        running = True

button_map = {5: "A",
              6: "B",
              16: "X",
              24: "Y"}

button_a = Button(5)
button_b = Button(6)
button_x = Button(16)
button_y = Button(24)

try:
    button_a.when_pressed = pressed
    button_b.when_pressed = pressed
    button_x.when_pressed = pressed
    button_y.when_pressed = pressed

    pause()

except KeyboardInterrupt:
    button_a.close()
    button_b.close()
    button_x.close()
    button_y.close()



while running:

    sentence=input('Please enter a sentence: ')
    scored = analyzer.polarity_scores(sentence)['compound']

    if scored >= 0.2:
        set=2
    elif scored<=-0.2:
        set=3
    else:
        set=1

    __color_set__()
    time.sleep(7)
    running = False
    set = 4

while not running:
    for x in range(17):
        for y in range(7):
            uh.set_pixel(x, y, 255, 255, 0)
    uh.show()
    time.sleep(0.25)
    uh.clear()
    uh.show()
    time.sleep(0.25)
