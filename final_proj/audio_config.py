import speech_recognition as sr

r = sr.Recognizer
mic = sr.Microphone(2)

with mic as source:
  r.adjust_for_ambient_noise(source)
  audio = r.listen(source)
r.recongnize_google(audio)
