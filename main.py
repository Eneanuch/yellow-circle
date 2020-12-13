from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication
from random import randint
from PyQt5 import QtCore, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(317, 379)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(100, 260, 121, 23))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 317, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Круг (не квадрат)"))
        self.pushButton.setText(_translate("MainWindow", "Кнопка (на месте)"))


class Main(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.draw_circle = 0

        self.setupUi(self)
        self.pushButton.clicked.connect(self.do_circles)

    def do_circles(self):
        self.draw_circle = 1
        self.repaint()

    def draw_circles(self, qp):
        if self.draw_circle:
            self.draw_circle = 0
            for i in range(randint(0, 10)):
                radius, x, y = randint(10, 100), randint(0, 260), randint(0, 250)
                qp.setBrush(QColor(255, 255, 0))
                qp.drawEllipse(x, y, radius, radius)

    def paintEvent(self, event):
        qp = QPainter()

        qp.begin(self)
        self.draw_circles(qp)
        qp.end()


if __name__ == "__main__":
    from sys import argv, exit

    app = QApplication(argv)
    ex = Main()
    ex.show()
    exit(app.exec_())