import random
import sys
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QApplication, QMainWindow,QWidget, QGraphicsBlurEffect, QGraphicsDropShadowEffect
from pyautogui import position

class Circle(QMainWindow):
    def __init__(self):
        super().__init__(flags=Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnBottomHint | Qt.WindowType.Tool)
        self.tracker = QWidget(self)
        self.tracker.geometry()
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.seek_pos)
        self.timer.start(50)
        self.timercol = QTimer(self.tracker)
        self.timercol.timeout.connect(self.changecolor)
        self.timercol.start(200)
        self.setStyleSheet("*{background-color:transparent;}")
        blur = QGraphicsBlurEffect()
        blur.setBlurRadius(40)
        self.tracker.setGraphicsEffect(blur)
        self.changecolor()
        self.seek_pos()
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.show()

    def seek_pos(self):
        pos = position()
        self.tracker.setGeometry(pos.x-45, pos.y-45, 100, 100)        

    def changecolor(self):
        new_color = QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        # Set the background color of the widget
        self.tracker.setStyleSheet(f"background-color: {new_color.name()}; border-radius: 45px;")
        self.raise_()

def main():
    app = QApplication(sys.argv)
    window = Circle()
    window.showFullScreen()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()