from kivymd.app import MDApp
from kivymd.uix.button import MDFlatButton
from kivymd.uix.list import OneLineListItem
from kivymd.uix.dialog import MDDialog
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager
from kivy.lang import Builder
from kivy.core.clipboard import Clipboard

from measure.metrics import Metric, explained
from config import *

Builder.load_file('gui.kv')


class User(MDScreen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.dialog = None

    def submit(self):
        c_11 = self.ids.TP.text
        c_00 = self.ids.TN.text
        c_10 = self.ids.FN.text
        c_01 = self.ids.FP.text

        if (c_11 != '' and c_11.isnumeric()) and \
                (c_10 != '' and c_10.isnumeric()) and \
                (c_01 != '' and c_01.isnumeric()) and \
                (c_00 != '' and c_00.isnumeric()):

            metrics = Metric(c_11=int(c_11), c_00=int(c_00), c_10=int(c_10), c_01=int(c_01))

            results = metrics.all_metrics()

            self.ids.container.clear_widgets()

            for k, v in results.items():
                self.ids.container.add_widget(
                    OneLineListItem(text=f'[b] {k}: [/b] {v} \n', on_release=self._get_measure_explain)
                )

    def _clean_text(self, text):
        textsplit = text.split(' ')
        textsplit = [word for word in textsplit if word not in ['[b]', '[/b]']]
        result = ' '.join(textsplit)

        return result

    def _copy_text_to_clipboard(self, measure):
        text = measure.text
        result = self._clean_text(text)
        Clipboard.copy(result)

    def _get_measure_explain(self, measure):
        text = measure.text
        result = self._clean_text(text)
        measure_type = result.split(' ')[0].split(':')[0]

        self.dialog = MDDialog(
                text=explained[measure_type],
            )
        self.dialog.open()

    def clear(self):
        self.ids.TP.text = ''
        self.ids.TN.text = ''
        self.ids.FN.text = ''
        self.ids.FP.text = ''


class RootWidget(MDScreenManager):
    pass


class Main(MDApp):

    def build(self):
        self.title = "Measure calculator"
        return RootWidget()


if __name__ == '__main__':
    kv = Main()
    kv.run()
