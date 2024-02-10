import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QWidget


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('My App')
        
        # Cannot set QxxLayout directly on the QMainWindow
        # Need to create a QWidget and set it as the central widget
        widget = QWidget()
        layout = QVBoxLayout()
        b1 = QPushButton('Red'   ); b1.setStyleSheet("background-color: red;")
        b2 = QPushButton('Blue'  ); b2.setStyleSheet("background-color: blue;")
        b3 = QPushButton('Yellow'); b3.setStyleSheet("background-color: yellow;")
        layout.addWidget(b1)
        layout.addWidget(b2)
        layout.addWidget(b3)
            
        widget.setLayout(layout)
        self.setCentralWidget(widget)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()