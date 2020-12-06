from random import randrange as rdrg
import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.QtGui import QPainter, QColor


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(511, 300)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(410, 260, 93, 28))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "Draw"))


class App(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.x, self.y = rdrg(40, 200), rdrg(40, 200)
        self.color1 = (rdrg(0, 255), rdrg(0, 255), rdrg(0, 255))
        self.color2 = (rdrg(0, 255), rdrg(0, 255), rdrg(0, 255))
        self.b_c = False
        self.pushButton.clicked.connect(self.draw_circles)

    def draw_circles(self):
        self.b_c = True
        self.repaint()
        self.b_c = False

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)

        if self.b_c:
            self.x, self.y = rdrg(40, 200), rdrg(40, 200)
            self.color1 = (rdrg(0, 255), rdrg(0, 255), rdrg(0, 255))
            self.color2 = (rdrg(0, 255), rdrg(0, 255), rdrg(0, 255))

        x, y, col1, col2 = self.x, self.y, self.color1, self.color2

        qp.setBrush(QColor(*col1))
        qp.drawEllipse(130 - x // 2, 130 - x // 2, x, x)

        qp.setBrush(QColor(*col2))
        qp.drawEllipse(390 - y // 2, 130 - y // 2, y, y)
        qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec_())