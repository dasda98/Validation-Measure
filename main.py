from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder

from measure.metrics import Metric


Builder.load_file('gui.kv')

Window.clearcolor = (1, 1, 1, 1.0)
Window.size = (800, 600)


class User(Screen):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def submit(self):
        c_11 = int(self.ids.TP.text)
        c_00 = int(self.ids.TN.text)
        c_10 = int(self.ids.FN.text)
        c_01 = int(self.ids.FP.text)
        
        metrics = Metric(c_11=c_11, c_00=c_00, c_10=c_10, c_01=c_01)

        results = metrics.all_metrics()
        to_gui_label = ""

        for k, v in results.items():
            to_gui_label += f'{k}: {v} \n'


        self.ids.results_measure.text = str(to_gui_label)


class RootWidget(ScreenManager):
    pass


class Main(App):
    
    def build(self):
        return RootWidget()


if __name__ == '__main__':
    kv = Main()
    kv.run()
