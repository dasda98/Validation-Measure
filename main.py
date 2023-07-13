from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder


Builder.load_file('gui.kv')

Window.clearcolor = (0, 0.6, 0.1, 1.0)
Window.size = (600, 400)

class User(Screen):
    pass


class RootWidget(ScreenManager):
    pass


class Main(App):
    
    def build(self):
        return RootWidget()


if __name__ == '__main__':
    kv = Main()
    kv.run()
