from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

def start():
    app = QApplication(sys.argv)
    app.setApplicationName('Language Into Flashcard Tool')
    app.setFont(QFont('Microsoft Sans Serif', 12))
    from ui.interface import Interface
    form = Interface(app)
    form.show()
    app.exec_()


if __name__ == '__main__':
    start()
