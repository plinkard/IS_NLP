import sys
import os
import pandas as pd
import nltk
nltk.download('punkt')
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer= SentimentIntensityAnalyzer()

sentence = "This is a great VADER Example"
analyzer.polarity_scores(sentence)['compound']
