import random
import time
from unicornhatmini import UnicornHATMini
import nltk
from textblob import TextBlob
from ntlk.sentiment.vader import SentimentIntensityAnalyzer
#nltk.download('vader_lexicon')


analyzer= SentimentIntensityAnalyzer()

uh = UnicornHATMini()

uh.set_brightness(0.5)


set = 0

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



running = True

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
