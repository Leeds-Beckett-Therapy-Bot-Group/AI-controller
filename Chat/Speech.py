import datetime
import json
import os

import pandas as pd
from gtts import gTTS
from playsound import playsound
from pocketsphinx import LiveSpeech, get_model_path


# this class handles speech recognition

class LanguageProcessor:
    def __init__(self):
        self.tracker = []
        self.sent_tracker = []
        self.phrase = str

    # this tracks certain values through a question
    # and answer phase, this happens once a session
    # and creates a JSON for the purpose of tracking
    # progress long term
    def mood_detector(self):
        questions = ["Hello, would you mind answering a few quick questions for me?",
                     "On a scale of one to ten, how happy do you feel today?",
                     "On a scale of one to ten, how confident do you feel today?",
                     "On a scale of one to ten, how sociable have you been today?",
                     "On a scale of one to ten, how active were you today?",
                     "On a scale of one to ten, how clean would you say your room is today?",
                     "Thanks for answering today! Here is some tasks you could do..."]
        question_replies = ["One? That's quite low, let's do some work on this",
                            "Two? It's pretty low, but let's be positive",
                            "Three? Quite low, but we can work on this ",
                            "Four? Fairly lowish, we can make some improvement here ",
                            "Five? Okay, keep up the good work but we can improve",
                            "Six?, Good work, let's focus on doing better",
                            "Seven? Wow, you're on a role, keep up the good work",
                            "Eight? Amazing, you're doing really well at this ",
                            "Nine?, Outstanding, you can't do much better than this",
                            "Ten?, You have reached god mode, no more improvement can be made"]
        answers = []

        for i in range(1, 6):
            text_to_speech = gTTS(text=questions[i], lang='en')
            audio = str("sound" + str(i) + ".mp3")
            text_to_speech.save(audio)
            playsound(audio)
            os.remove("sound" + str(i) + ".mp3")

            for phrase in LiveSpeech():
                if 'one' or 'two' or 'three' or 'four' or 'five' or 'six' or 'seven' or 'eight' or 'nine' or 'ten' in phrase:
                    print(phrase)

                    try:
                        int(phrase)

                        for j in range(0):
                            text_to_speech = gTTS(text=question_replies[phrase], lang='en')
                            audio = str("answer.mp3")
                            text_to_speech.save(audio)
                            playsound(audio)
                            os.remove("answer.mp3")

                    except:
                        print("phrase was not an integer..")

                        text_to_speech = gTTS(text="Please say a number between one and ten", lang='en')
                        audio = str("error.mp3")
                        text_to_speech.save(audio)
                        playsound(audio)
                        os.remove("error.mp3")

        mood = [{'index': len(self.tracker) + 1,
                 'timestamp': str(datetime.datetime.now()),
                 'happiness': answers[0],
                 'community': answers[1],
                 'confidence': answers[2],
                 'cleanliness': answers[3],
                 'activeness': answers[4]}]
        self.tracker.append(mood)

        with open('mood.txt', 'a') as outfile:
            json.dump(mood, outfile, indent=4)

        return mood

    # use this to track negative and positive words
    # over the course of the interaction, can be used
    # to tailor the conversation
    def sentiment_tracker(self):
        sentiment = [{'index': len(self.tracker) + 1,
                      'timestamp': str(datetime.datetime.now()),
                      'positive': str(),
                      'negative:': str()}]
        self.sent_tracker.append(sentiment)

        with open('sentiment.txt', 'a') as outfile:
            json.dump(sentiment, outfile, indent=4)

        return sentiment

    def sentiment_analysis(self):
        print("todo")

    def convert_json_to_graph(self):
        graph = pd.DataFrame(self.tracker['mood'])
        print(graph)

    def speech_to_text(self, phrase):
        for phrase in LiveSpeech():
            print(phrase)

        return phrase

    def bot_talk(self):
        text_to_speech = gTTS(text="hello", lang='en')
        audio = "sound.mp3"
        text_to_speech.save(audio)
        playsound(audio)
        return audio
