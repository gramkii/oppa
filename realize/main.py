from PyQt5.QtWidgets import * 
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from random import *
import time
import sys 
import string
#app = QApplication([])

#window = QWidget()
#window.setWindowTitle("Тренування друку")
#window.resize(700,500)


#start_test = QPushButton("Почати тест")
#restart_test = QPushButton("Спробувати знову")

#user_input = QLineEdit()
#word_label = QLabel("")
#result = QLabel()

class Trainer(QWidget):
    def __init__(self):
        super().__init__()
        self.init_Gui()
    
    def init_Gui(self):
        self.start_test = QPushButton("Почати тест", self)
        self.start_test.clicked.connect(self.start_training)
        self.user_input = QLineEdit(self)
        self.word_label = QLabel("", self)
        self.word_label.setStyleSheet('font-size: 19px; font-weight: bold;')
        self.result = QLabel("", self)
        layout = QVBoxLayout()
        layout.addWidget(self.start_test)
        layout.addWidget(self.user_input)
        layout.addWidget(self.word_label)
        layout.addWidget(self.result)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.check)
        self.setLayout(layout)
        self.resize(700, 500)
        self.show()

    def choose_word(self):
        choosed_word = choice(["skoro.txt", "skoro2.txt", "skoro3.txt", "skoro4.txt"])
        with open (choosed_word, "r", encoding="UTF-8") as file:
            word = file.read()
        print(word)


        return word

    def generate_random_word(self):
        return ''.join(choice(string.ascii_lowercase) for _ in range(5))

    def start_training(self):
        self.word_type = self.choose_word()
        self.word_length = len(self.word_type)
        self.word_label.setText(self.word_type)
        self.user_input.clear()
        self.result.clear()
        #self.start_test(False)
        self.timer.start(100)
        self.timestart = time.time()
        





    def check(self):
        user_input = self.user_input.text()
        if user_input == self.word_type:
            self.timeend = time.time()
            self.timewrite = (self.timeend-self.timestart)/60
            self.result.setText("Правильно! Ваша швидкість: " + str(int(self.word_length/self.timewrite)) + " символи в хвилину")
            self.timer.stop()
            


        else:
            self.result.clear()
            
if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet("""
    QWidget {
        background: #337CCF;
    }

    QPushButton
    {
        background: #FFC436;
        border-width: 7px;
        border-color: #191D88;
        border-style: inset;
        font-family: Arial;
    }
    QLabel {
        font-family: Arial;
    }
    QLineEdit {
        font-family: Arial; 
        font-size: 16px;
    }
""")
    trainer = Trainer()
    sys.exit(app.exec_())

#trainer = Trainer()






#window.show()
app.exec_()