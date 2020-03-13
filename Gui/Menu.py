import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle, Color
from kivy.config import Config

Config.set('graphics', 'width', '720')
Config.set('graphics', 'height', '720')


class BackgroundScreen(Widget):
    def __init__(self, **kwargs):
        super(BackgroundScreen, self).__init__(**kwargs)

        with self.canvas:
            Color(1, 0, 0, 1)

            self.rect = Rectangle(pos=self.pos, size=self.size,
                                  source='Res/eyes-closed-left.png',)


class Psycube(App):
    def build(self):
        return BackgroundScreen()
