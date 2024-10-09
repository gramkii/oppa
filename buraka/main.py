from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

from kivy.uix.screenmanager import Screen, ScreenManager

class FirstScr(Screen):
    def __init__(self, name = "first"):
        super().__init__(name=name)
        btn = Button(text = "Натисність, щоб пройти перевірку")
        btn.on_press = self.next
        self.add_widget(btn)
    
    def next(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'second'


class SecondScr(Screen):
    def __init__(self, name = "second"):
        super().__init__(name=name)
        btn = Button(text = "Ура! Ви пройшли провірку!(Натисніть ще раз для повторної перевірки)")
        btn.on_press = self.next
        self.add_widget(btn)

    def next(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'first'

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(FirstScr())
        sm.add_widget(SecondScr())

        return sm
app = MyApp()
app.run()