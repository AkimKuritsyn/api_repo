import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel
import requests
from PIL import Image
from io import BytesIO


class Widget(QWidget):
    def __init__(self):
        super().__init__()
        w, h = 900, 650
        self.setGeometry(300, 100, w, h)

        apikey = "f3a0fe3a-b07e-4840-a1da-06f18b2ddf13"
        api_server = "http://static-maps.yandex.ru/v1"
        self.coord = (42.0426, 55.575)
        delta1 = "0.016457"
        delta2 = "0.00619"
        params = {
            "ll": ",".join([str(x) for x in self.coord]),
            "spn": ",".join([delta1, delta2]),
            "apikey": apikey,
        }
        response = requests.get(api_server, params=params)
        im = BytesIO(response.content)
        im = Image.open(im)







if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Widget()
    window.show()
    sys.exit(app.exec())
