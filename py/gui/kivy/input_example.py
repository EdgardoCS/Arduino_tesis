from kivy.app import App
from kivy.base import Builder
from kivy.properties import StringProperty, ObjectProperty
from kivy.uix.boxlayout import BoxLayout

Builder.load_string("""
<rootwi>:
    BoxLayout:
        orientation: 'vertical'
        textinputtext: txt.text
        obj_widget: w1
        BoxLayout:
            Button:
                on_press: root.print_txt()
            TextInput:
                id: txt
                text: root.textinputtext
<MyRootWidget@BoxLayout>:
    obj_widget: w1
    MyWidget:
        id: w1
        text: "purple turtle"
'''                
""")


class rootwi(BoxLayout):
    textinputtext = StringProperty()

    def __init__(self, **kwargs):
        super(rootwi, self).__init__(**kwargs)
        self.textinputtext = 'palim'

    def print_txt(self):
        print(self.obj_widget.textinputtext)


class MyApp(App):
    def build(self):
        return rootwi()


if __name__ == '__main__':
    MyApp().run()
