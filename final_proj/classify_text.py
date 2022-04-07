import sys
import os
import pandas as pd
import nltk
from textblob import TextBlob
from ntlk.sentiment.vader import SentimentIntensityAnalyzer
#nltk.download('vader_lexicon')

analyzer= SentimentIntensityAnalyzer()

sentence = "This is a great VADER Example"
print(analyzer.polarity_scores(sentence)['compound'])
