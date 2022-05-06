from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.windowTitleChanged.connect(self.onWindowTitleChange)
        self.windowTitleChanged.connect(lambda x: self.my_custom_fn())
        self.windowTitleChanged.connect(lambda x: self.my_custom_fn(x))
        self.windowTitleChanged.connect(lambda x: self.my_custom_fn(x, 25))
        self.setWindowTitle("PyQT5 App")

        label = QLabel("Usual Label")
        label.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(label)

    def onWindowTitleChange(self, s):
        print(s)

    def my_custom_fn(self, a="Привет", b=5):
        print(a, b)

    def contextMenuEvent(self, event):
        print("Contex menu event!")


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()
