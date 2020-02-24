import cv2
from gtts import gTTS
from playsound import playsound
from pocketsphinx import LiveSpeech
import pandas as pd
import bluetooth
import sys
import json
import os
import datetime

from Chat.Speech import LanguageProcessor
from Visual.FaceDetection import VisualProcessor


class SoundProcessor:
    def startup(self):
        audio = ''
        playsound(audio)





class Main:
    while True:
        VisualProcessor().collect_dataset()
        #LanguageProcessor().key_word_detector()
        LanguageProcessor().mood_detector()

        # start gui
        # sleeping animation
        #

        # wake up sound

        # search for nearby bluetooth devices


        # if connected
        # receive json
        #

        #

        # VisualProcessor().visualrec()
        # BotScreen().build()


if __name__ == '__main__':
    Main()
