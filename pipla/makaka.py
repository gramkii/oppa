from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import pandas as pd 
import matplotlib.pyplot as pl 

df = pd.read_csv("GooglePlayStore_wild.csv")

app = QApplication([])
window = QWidget()
window.resize(700, 500)
window.setWindowTitle('DATA MUMURDIK')



window.show()
app.exec_()