from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic
from random import randint


class Main(QMainWindow):
    def __init__(self):
        super().__init__()

        self.draw_circle = 0

        uic.loadUi('UI.ui', self)
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
    # do window, if window closed, program will exit