from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.factory import Factory
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.core.audio import SoundLoader

import os

class LoadDialog(FloatLayout):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)

class Root(FloatLayout):

    text_input = ObjectProperty(None)

    def show_load(self):
        content = LoadDialog(load=self.load, cancel=self.dismiss_popup)
        self._popup = Popup(title="Load file", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def play(self):
        sound = SoundLoader.load(self.text_input.text)
        if sound:
            print("Sound found at %s" % sound.source)
            print("Sound is %.3f seconds" % sound.length)
            sound.play()

    def load(self, path, filename):
        print(path,filename)
        print(self.text_input)
        self.text_input.text = str(filename[0])
        self.dismiss_popup()

    def dismiss_popup(self):
        self._popup.dismiss()


Factory.register('LoadDialog', cls=LoadDialog)
Factory.register('Root', cls=Root)

class MainApp(App):
    kv_directory = 'template'


if __name__ == '__main__':
    app = MainApp()
    app.run()
