import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
import requests
from PIL import Image
from io import BytesIO

MAX_SCALE = 15
MIN_SCALE = 3


class Widget(QWidget):
    def __init__(self):
        super().__init__()
        w, h = 700, 450
        self.setGeometry(350, 100, w, h)

        apikey = "f3a0fe3a-b07e-4840-a1da-06f18b2ddf13"
        self.api_server = "http://static-maps.yandex.ru/v1"
        self.coord = [42.0426, 55.575]
        self.scale = 10
        self.move_r = 0.01

        self.params = {
            "ll": ",".join([str(x) for x in self.coord]),
            'z': f'{self.scale}',
            "apikey": apikey,
        }
        response = requests.get(self.api_server, params=self.params)
        im = BytesIO(response.content)
        im = Image.open(im)
        im.save('map.png')

        self.image = QPixmap('map.png')
        self.map = QLabel(self)
        self.map.move(100, 0)
        self.map.resize(w, h)
        self.map.setPixmap(self.image)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_PageUp:
            self.set_scale(1)
        elif event.key() == Qt.Key.Key_PageDown:
            self.set_scale(-1)
        else:
            x = y = 0
            di = {Qt.Key.Key_Left: (-self.move_r, 0), Qt.Key.Key_Right: (self.move_r, 0),
                  Qt.Key.Key_Up: (0, self.move_r), Qt.Key.Key_Down: (0, -self.move_r)}
            for ev in di:
                if event.key() == ev:
                    x += di[ev][0]
                    y += di[ev][1]
            if x or y:
                self.move(x, y)

    def move(self, x, y):
        self.coord[0] += x
        self.coord[1] += y

        self.set_image()

    def set_scale(self, n):
        self.scale += n
        if self.scale > MAX_SCALE:
            self.scale -= 1
        elif self.scale < MIN_SCALE:
            self.scale += 1
        self.set_image()

    def set_image(self):
        self.params["ll"] = ",".join([str(x) for x in self.coord])
        self.params['z'] = f'{self.scale}'

        response = requests.get(self.api_server, params=self.params)
        im = BytesIO(response.content)
        im = Image.open(im)
        im.save('map.png')
        self.image = QPixmap('map.png')
        self.map.setPixmap(self.image)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Widget()
    window.show()
    sys.exit(app.exec())
