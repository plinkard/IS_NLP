import os
import signal
import subprocess
import random
import time
import speech_recognition as sr

r=sr.Recognizer()

#mic = sr.Microphone(1) #mic index in parenthesis

proc_args = ['arecord', '-D' , 'plughw:1,0' , '--duration=10', 'test.wav']
rec_proc = subprocess.Popen(proc_args, shell=False, preexec_fn=os.setsid)
os.killpg(rec_proc.pid, signal.SIGTERM)

with sr.WavFile("test.wav") as source:
    r.adjust_for_ambient_noise(source)
    audio=r.record(source)
print(r.recognize_google(audio))
