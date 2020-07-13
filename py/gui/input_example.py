from kivy.app import App
from kivy.base import Builder
from kivy.properties import StringProperty, ObjectProperty
from kivy.uix.boxlayout import BoxLayout

Builder.load_string("""
<rootwi>:
    orientation: 'vertical'
    textinputtext: txt.text
    BoxLayout:
        Button:
            on_press: root.print_txt()
        TextInput:
            id: txt
            text: root.textinputtext
""")


class rootwi(BoxLayout):
    textinputtext = StringProperty()

    def __init__(self, **kwargs):
        super(rootwi, self).__init__(**kwargs)
        self.textinputtext = 'palim'

    def print_txt(self):
        print(self.textinputtext)


class MyApp(App):
    def build(self):
        return rootwi()


if __name__ == '__main__':
    MyApp().run()
