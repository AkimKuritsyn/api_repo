import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel
import requests


class Widget(QWidget):
    def __init__(self):
        super().__init__()
        w, h = 900, 650
        self.setGeometry(300, 100, w, h)

        self.coord = 0, 0


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Widget()
    window.show()
    sys.exit(app.exec())
