from random import randrange as rdrg
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.QtGui import QPainter, QColor


class App(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)

        self.x, self.y = rdrg(40, 200), rdrg(40, 200)
        self.b_c = False
        self.pushButton.clicked.connect(self.draw_circles)

    def draw_circles(self):
        self.b_c = True
        self.repaint()
        self.b_c = False

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        qp.setPen(QColor(220, 220, 0))
        qp.setBrush(QColor(220, 220, 0))
        if self.b_c:
            self.x, self.y = rdrg(40, 200), rdrg(40, 200)

        x, y = self.x, self.y

        qp.drawEllipse(130 - x // 2, 130 - x // 2, x, x)
        qp.drawEllipse(390 - y // 2, 130 - y // 2, y, y)
        qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec_())