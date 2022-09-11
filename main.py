from kivy.app import App
from kivy.uix.button import Button
from kivy.config import Config
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

from kivy.uix.gridlayout import GridLayout


Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '500')

class CalcApp(App):
    def update_label(self):
        self.label.text = self.formula

    def add_number(self, instance):
        if self.formula == "0":
            self.formula = ""
        self.formula += str(instance.text)
        self.update_label()

    def add_operation(self, instance):
        if str(instance.text) == 'x':
            self.formula += '*'
        else:
            self.formula += str(instance.text)
        self.update_label()

    def clear_label(self, instance):
        self.formula = "0"
        self.update_label()

    def calc_result(self, instance):
        self.label.text = str(eval(self.label.text))
        self.formula = "0"

    def build(self):
        self.formula = "0"
        bl = BoxLayout(orientation='vertical')
        self.label = Label(text='0',
                            size_hint=[1, .4],
                            color=(.5,.5,.9, 1),
                            font_size=42,
                            pos_hint={'center_x': 0.5, 'center_y': 0.5},
                            halign='right',
                            text_size=(400 - 25, 500 * .4 - 25),
                            )

        bl.add_widget(self.label)
        gl = GridLayout(cols=4, spacing=[1], size_hint = (1, .6))

        gl.add_widget(Button(text='7', font_size=42, on_press=self.add_number))
        gl.add_widget(Button(text='8', font_size=42, on_press=self.add_number))
        gl.add_widget(Button(text='9', font_size=42, on_press=self.add_number))
        gl.add_widget(Button(text='x', font_size=42, on_press=self.add_operation))

        gl.add_widget(Button(text='4', font_size=42, on_press=self.add_number))
        gl.add_widget(Button(text='5', font_size=42, on_press=self.add_number))
        gl.add_widget(Button(text='6', font_size=42, on_press=self.add_number))
        gl.add_widget(Button(text='-', font_size=42, on_press=self.add_operation))

        gl.add_widget(Button(text='1', font_size=42, on_press=self.add_number))
        gl.add_widget(Button(text='2', font_size=42, on_press=self.add_number))
        gl.add_widget(Button(text='3', font_size=42, on_press=self.add_number))
        gl.add_widget(Button(text='+', font_size=42, on_press=self.add_operation))

        gl.add_widget(Button(text='C', font_size=42, on_press=self.clear_label))
        gl.add_widget(Button(text='0', font_size=42, on_press=self.add_number))
        gl.add_widget(Button(text='.', font_size=42, on_press=self.add_operation))
        gl.add_widget(Button(text='=', font_size=42, on_press=self.calc_result))

        bl.add_widget(gl)
        return bl

if __name__ == '__main__':
    CalcApp().run()
