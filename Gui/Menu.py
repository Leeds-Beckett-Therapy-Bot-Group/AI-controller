import kivy
from kivy import Config
from kivy.app import App
from kivy.uix.label import Label

# this class builds the GUI

class BotScreen(App):

    Config.set('graphics', 'width', '720')
    Config.set('graphics', 'height', '720')

    def build(self):
        return Label(text="Hello Lucy!")


BotScreen().run()
