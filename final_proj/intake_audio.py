"""
must also get beforehand:
pip apt-get install SpeechRecognition
pip apt-get install pyaudio
and may also need to install flac (use pip)
also use 'sr.Microphone.list_microphone_names()' to figure out which mic to use, and use the mic's index
sudo apt-get install espeak python-espeak

"""

"""
run 'sudo amixer cset numid=3 1', for final digit 0=auto, 1=3.5mm and 2=HDMI and 'sudo amixer sset PCM,0 100%'
"""

import random
import time
from espeak import espeak
import speech_recognition as sr



mic = sr.Microphone(1) #mic index in parenthesis
def recognize_speech_from_mic(recognizer, microphone):
    """Transcribe speech from recorded from `microphone`.

    Returns a dictionary with three keys:
    "success": a boolean indicating whether or not the API request was
               successful
    "error":   `None` if no error occured, otherwise a string containing
               an error message if the API could not be reached or
               speech was unrecognizable
    "transcription": `None` if speech could not be transcribed,
               otherwise a string containing the transcribed text
    """
    # check that recognizer and microphone arguments are appropriate type
    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError("`recognizer` must be `Recognizer` instance")

    if not isinstance(microphone, sr.Microphone):
        raise TypeError("`microphone` must be `Microphone` instance")

    # adjust the recognizer sensitivity to ambient noise and record audio
    # from the microphone
    with mic as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    # set up the response object
    response = {
        "success": True,
        "error": None,
        "transcription": None
    }
    # tries recognizing the speech in the recording
    # if a RequestError or UnknownValueError exception is caught,
    #     update the response object accordingly
    try:
        response["transcription"] = recognizer.recognize_google(audio)
    except sr.RequestError:
        # API was unreachable or unresponsive
        response["success"] = False
        response["error"] = "API unavailable"
    except sr.UnknownValueError:
        # speech was unintelligible
        response["error"] = "Unable to recognize speech"

    return response

recognizer = sr.Recognizer()
microphone = sr.Microphone()

espeak -ven+f1 -s 200 -a 100 "Hello! Please say a sentence"

gotten = False
while not gotten:
        statement = recognize_speech_from_mic(recognizer, microphone)
        if statement["error"]:
                print("ERROR: {}".format(statement["error"])
                espeak -ven+f1 -s 200 -a 100 "Sorry, there was an error. Error is {}".format(statement["error"])
                break
        if statement["transcription"]:
            gotten = True
            break
        if not statement["success"]:
            gotten = True
            break
        print("I didn't catch that. What did you say?\n")
        espeak -ven+f1 -s 200 -a 100 "I didn't catch that. What did you say?\n"

espeak -ven+f1 -s 200 -a 100 "You said {}".format(statement["transcription"])
