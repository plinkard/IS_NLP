
import os
import signal
import subprocess
import random
import time
import speech_recognition as sr

r=sr.Recognizer()

mic = sr.Microphone(1) #mic index in parenthesis


with mic as source:
    r.adjust_for_ambient_noise(source)
    audio=r.listen(source)
print(r.recognize_google(audio))
