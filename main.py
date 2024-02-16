# import module 
import sys, cv2, datetime, win32gui, win32con, random
from PyQt5.QtCore import Qt, pyqtSlot, QUrl, QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow,QWidget, QDesktopWidget, QGraphicsBlurEffect
from PyQt5.QtMultimedia import QAudioOutput, QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
from pyautogui import position
from PyQt5.QtGui import QColor
from sd import TimeWindow
from test import Circle


filename = "loopGrass.mp4"
# create video capture object 
data = cv2.VideoCapture(filename) 

# count the number of frames 
frames = data.get(cv2.CAP_PROP_FRAME_COUNT) 
fps = data.get(cv2.CAP_PROP_FPS) 

# calculate duration of the video 
seconds = round(frames / fps)
video_time = datetime.timedelta(seconds=seconds) 
print(f"duration in seconds: {seconds}") 
print(f"video time: {video_time}") 



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        width = QDesktopWidget().width()
        height = QDesktopWidget().height()
        self._audio_output = QAudioOutput()
        # self.timer = QTimer(self)
        # self.timer.timeout.connect(self.active)
        # self.timer.start(3000)
        self.player = QMediaPlayer()
        # self.active()
        self.player.setPlaybackRate(1.0)  # Set default playback rate
        self.player.positionChanged.connect(self.check_position)
        self._video_widget = QVideoWidget()
        self.setCentralWidget(self._video_widget)
        self.player.setVideoOutput(self._video_widget)
        self.open()
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint, True)
        self.setWindowFlag(Qt.WindowType.WindowStaysOnBottomHint, False)
        self.setWindowFlag(Qt.WindowType.WindowTransparentForInput, True)
        self.setWindowFlag(Qt.WindowType.Tool, True)
        # print(str(QTime.currentTime().hour()) + ":" + str(QTime.currentTime().minute()) )

    def open(self, url=QUrl(filename)):
        self.player.setMedia(QMediaContent(url))
        self.player.play()

    @pyqtSlot()
    def check_position(self):
        # Check if the video has reached its end
        if self.player.state() == QMediaPlayer.State.StoppedState:
            self.player.setPosition(0)  # Seek back to the beginning
            self.player.play()

    def show_status_message(self, message):
        self.statusBar().showMessage(message, 5000)

    @pyqtSlot("QMediaPlayer::Error", str)
    def player_error(self, error, error_string):
        print(error_string, file=sys.stderr)
        self.show_status_message(error_string)

    # def active(self):
    #     print(int(self.winId()))
    #     forground = win32gui.GetForegroundWindow()
    #     taskbar = win32gui.FindWindow("Shell_TrayWnd", None)
    #     if forground == int(self.winId()) or forground == taskbar:
    #     # if forground == int(self.winId()):

    #         win32gui.ShowWindow(taskbar, win32con.SW_FORCEMINIMIZE)
    #         # win32gui.SetActiveWindow(int(self.winId()))
    #     # else:
    #     #     self.player.pause()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.showFullScreen()
    time = TimeWindow()
    time.show()
    circle = Circle()
    circle.showFullScreen()
    main_win.setWindowFlag(Qt.WindowType.WindowStaysOnBottomHint, True)
    
    sys.exit(app.exec())
