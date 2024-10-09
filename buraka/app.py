from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout

p1, p2, p3 = 0, 0, 0
name, age = '', 10

from ruffier import *
from instructions import *

class Login(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        textLogin = Label(text = "Введіть логін")
        textPassword = Label(text = "Введіть пароль")
        self.login = TextInput(multiline = False)
        self.password = TextInput(multiline = False)


        linelogin = BoxLayout()
        linelogin.add_widget(textLogin)
        linelogin.add_widget(self.login)
        
        linePassword = BoxLayout()
        linePassword.add_widget(textPassword)
        linePassword.add_widget(self.password)

        self.btn = Button(text = "Ввійти")
        main_layout = BoxLayout(orientation = 'vertical', padding = 8, spacing = 8)
        main_layout.add_widget(lineLogin)
        main_layout.add_widget(linePassword)

        main_layout.add_widget(self.btn)
        self.add_widget(main_layout)

class InstructionScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        instr = Label(text = txt_instruction)
        lblName = Label(text = "Введіть ім'я")
        lblage = Label(text = "Введіть вік")
        self.inputName = TextInput(multiline = False)
        self.inputAge = TextInput(multiline = False)
        self.btn = Button(text = "Почати")
        self.btn.on_press = self.next

        lineName = BoxLayout()
        lineAge = BoxLayout()
        lineName.add_widget(lblName)
        lineName.add_widget(self.inputName)

        lineAge.add_widget(lblage)
        lineAge.add_widget(self.inputAge)
        
        main_layout = BoxLayout(orientation = 'vertical', padding = 8, spacing = 8)
        main_layout.add_widget(instr)        
        main_layout.add_widget(lineName)
        main_layout.add_widget(lineAge)
        main_layout.add_widget(self.btn)
        self.add_widget(main_layout)

    def next(self):
        global name
        name = self.inputName.text
        self.manager.current = 'pulse1'

class Pulse1(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        instr = Label(text = txt_test1)
        lblPulse = Label(text = "Введіть пульс")
        self.inputPulse = TextInput(multiline = False)
        self.btn = Button(text = "Продовжити")
        self.btn.on_press = self.next

        linePulse = BoxLayout()
        linePulse.add_widget(lblPulse)
        linePulse.add_widget(self.inputPulse)

        main_layout = BoxLayout(orientation = 'vertical', padding = 8, spacing = 8)
        main_layout.add_widget(instr)        
        main_layout.add_widget(linePulse)
        main_layout.add_widget(self.btn)
        self.add_widget(main_layout)

    def next(self):
        global p1
        p1 = int(self.inputPulse.text)
        self.manager.current = 'sits'
    
class Sits(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        instr = Label(text = txt_sits)
        self.btn = Button(text = "Продовжити")
        self.btn.on_press = self.next

        main_layout = BoxLayout(orientation = 'vertical', padding = 8, spacing = 8)
        main_layout.add_widget(instr)
        main_layout.add_widget(self.btn)
        self.add_widget(main_layout)

    def next(self):
        self.manager.current = 'pulse2'

class Pulse2(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        instr = Label(text = txt_test3)
        resultAfter = Label(text = "Результат:")
        resultRest = Label(text = "Результат після відпочинку")
        self.inputAfter = TextInput(multiline = False)
        self.inputRest = TextInput(multiline = False)
        self.btn = Button(text = "Завершити")
        self.btn.on_press = self.next

        line1 = BoxLayout()
        line1.add_widget(resultAfter)
        line1.add_widget(self.inputAfter)

        line2 = BoxLayout()
        line2.add_widget(resultRest)
        line2.add_widget(self.inputRest)

        main_layout = BoxLayout(orientation = 'vertical', padding = 8, spacing = 8)
        main_layout.add_widget(instr)
        main_layout.add_widget(line1)
        main_layout.add_widget(line2)
        main_layout.add_widget(self.btn)

        self.add_widget(main_layout)
    
    def next(self):
        global p2, p3
        p2 = int(self.inputAfter.text)
        p3 = int(self.inputRest.text)
        self.manager.current = 'result'
    
class Result(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.main_layout = BoxLayout(orientation = 'vertical', padding = 8, spacing = 8)
        self.instr = Label(text = '')
        self.main_layout.add_widget(self.instr)

        self.add_widget(self.main_layout)
        self.on_enter = self.resultShow

    def resultShow(self):
        global name
        self.instr.text = name + '\n' + test(p1, p2, p3, age)





class Building(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(InstructionScreen(name='instruction'))
        sm.add_widget(Pulse1(name='pulse1'))
        sm.add_widget(Sits(name='sits'))
        sm.add_widget(Pulse2(name='pulse2'))
        sm.add_widget(Result(name='result'))
        return sm

app = Building()
app.run()

