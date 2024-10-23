# import module
import sys, cv2, datetime, win32gui, win32con
from PyQt5.QtCore import Qt, QTimer, QDate, QTime
from PyQt5.QtWidgets import (
    QMainWindow,
    QLabel,
    QVBoxLayout,
    QWidget,
    QDesktopWidget,
    QApplication,
)


class TimeWindow(QMainWindow):
    def __init__(self):
        width = QDesktopWidget().width()
        height = QDesktopWidget().height()
        super().__init__(flags=Qt.WindowType.FramelessWindowHint | Qt.WindowType.Tool)
        now = QDate.currentDate()
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.timer2 = QTimer(self)
        self.timer2.start(60000)
        self.mainwidget = QWidget()
        layout = QVBoxLayout()
        self.timeText = QLabel()
        self.DateText = QLabel()
        self.timer2.timeout.connect(self.CHANGETIME)
        self.setGeometry(self.timeText.geometry())
        self.timeText.setParent(self)
        self.DateText.setParent(self)
        self.timeText.setText(
            str(QTime.currentTime().hour()) + ":" + str(QTime.currentTime().minute())
        )
        self.DateText.setText(now.toString(Qt.DateFormat.DefaultLocaleLongDate))
        self.DateText.adjustSize()
        self.timeText.adjustSize()
        self.adjustSize()
        self.mainwidget.adjustSize()
        self.timeText.setStyleSheet(
            "font: bold; font-size:54px; color:white; font-family: 'Game of squids'; margin-left:50%; margin-"
        )
        self.DateText.setStyleSheet(
            "font: bold; font-size:28px; color:white; font-family: 'Game of squids';"
        )
        layout.addWidget(self.timeText)
        layout.addWidget(self.DateText)
        self.mainwidget.setLayout(layout)
        self.setCentralWidget(self.mainwidget)
        print(width // 2, height // 2)
        self.timeText.setGeometry(
            width // 2, height // 2, self.geometry().width(), self.geometry().height()
        )
        self.mainwidget.setGeometry(
            width // 2, height // 2, self.geometry().width(), self.geometry().height()
        )
        self.timeText.setGeometry(
            width // 2, height // 2, self.geometry().width(), self.geometry().height()
        )
        self.DateText.setGeometry(
            width // 2, height // 2, self.geometry().width(), self.geometry().height()
        )
        # self.show()
        self.raise_()

    def CHANGETIME(self):
        self.timeText.setText(
            str(QTime.currentTime().hour()) + ":" + str(QTime.currentTime().minute())
        )
        self.DateText.setText(
            QDate.currentDate().toString(Qt.DateFormat.DefaultLocaleLongDate)
        )
        self.raise_()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TimeWindow()
    window.show()
    sys.exit(app.exec_())
# import cv2
# def save_first_frame(video_path, output_path):
#     # Open the video file
#     cap = cv2.VideoCapture(video_path)

#     # Check if the video opened successfully
#     if not cap.isOpened():
#         print("Error: Could not open video.")
#         return

#     # Read the first frame
#     ret, frame = cap.read()

#     # Check if the frame was read successfully
#     if not ret:
#         print("Error: Could not read frame.")
#         return

#     # Save the first frame as an image
#     cv2.imwrite(output_path, frame)
#     print("First frame saved as", output_path)

#     # Release the video capture object
#     cap.release()

# if __name__ == "__main__":
#     video_path = input("Enter the path to the video file: ")
#     output_path = input("Enter the path to save the first frame (include file extension): ")
#     save_first_frame(video_path, output_path)
