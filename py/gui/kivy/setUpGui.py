from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty, ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.anchorlayout import AnchorLayout

Builder.load_string("""
<Boxes>:
    AnchorLayout:
        anchor_x: 'center'
        anchor_y: 'top'
        size_hint: 1, .9
        BoxLayout: 
            orientation: 'vertical'
            padding: 10

            BoxLayout:
                padding: 10
                orientation: 'horizontal'
                textinputtext1: txt1.text
                textinputtext2: txt2.text
                textinputtext3: txt3.text
                
                Button:
                    size_hint: 0.5,0.5
                    on_press: root.print_txt()
                    text:'Set velocities'
                TextInput:
                    font_size: 40
                    id: txt1
                    text: root.textinputtext1
                    
                Button:
                    on_press: root.print_txt()
                    text:'Set samples'
                TextInput:
                    id: txt2
                    text: root.textinputtext2  
                     
                Button:
                    on_press: root.print_txt()
                    text:'Set pause'
                TextInput:
                    id: txt3
                    text: root.textinputtext3
      
            BoxLayout:
                orientation: 'horizontal'
                Button:
                    text: "2"
                Button:
                    text: "3"
                Button:
                    text: "4"
            BoxLayout:
                orientation: 'horizontal'
                Button:
                    text: "5"
                Button:
                    text: "6"
            BoxLayout:
                orientation: 'horizontal'
                Button:
                    text: "7"
                Button:
                    text: "8"
                Button:
                    text: "9"
                Button:
                    text: "10"
    AnchorLayout:
        anchor_x: 'center'
        anchor_y: 'bottom'
        BoxLayout:
            orientation: 'horizontal'
            size_hint: 1, .1
            Button:
                text: 'Go to Screen 1'
                on_press: _screen_manager.current = 'screen1'
            Button:
                text: 'Go to Screen 1'
                on_press: _screen_manager.current = 'screen1'    
            Button:
                text: 'Go to Screen 1'
                on_press: _screen_manager.current = 'screen1'       
            Button:
                text: 'Go to Screen 2'
                on_press: _screen_manager.current = 'screen2'""")


class Boxes(FloatLayout):
    textinputtext1 = StringProperty()
    textinputtext2 = StringProperty()
    textinputtext3 = StringProperty()

    def __init__(self, **kwargs):
        super(Boxes, self).__init__(**kwargs)
        self.textinputtext1 = 'palim'
        self.textinputtext2 = '5'
        self.textinputtext3 = '20'

    def print_txt(self):
        print(self.textinputtext1)
        print(self.textinputtext2)
        print(self.textinputtext3)


class TestApp(App):
    def build(self):
        return Boxes()


if __name__ == '__main__':
    TestApp().run()
