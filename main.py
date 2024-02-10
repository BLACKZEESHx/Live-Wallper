# import module 
import sys, cv2, datetime, win32gui, win32con
from PyQt5.QtCore import Qt, pyqtSlot, QUrl, QTimer, QDate, QTime
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtMultimedia import QAudioOutput, QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
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
        now = QDate.currentDate()
        month = now.currentDate().shortMonthName(now.month(), now.MonthNameType.DateFormat)
        day = now.currentDate().shortDayName(now.day(), now.MonthNameType.StandaloneFormat)
        year = now.currentDate().year()
        self._audio_output = QAudioOutput()
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.active)
        self.timer.start(3)
        self.active()
        self._player = QMediaPlayer()
        self._player.setPlaybackRate(1.0)  # Set default playback rate
        self._player.positionChanged.connect(self.check_position)
        self._video_widget = QVideoWidget()
        self.setCentralWidget(self._video_widget)
        self._player.setVideoOutput(self._video_widget)
        self.open()
        print("d", now.toString(Qt.DefaultLocaleLongDate))
        self.timeTextW = QMainWindow(flags=Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnBottomHint)
        self.timeTextW.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.timeText = QLabel()
        self.timeTextW.setGeometry(self.timeText.geometry())
        self.timeText.setParent(self.timeTextW)
        self.timeTextW.show()
        self.timeText.setText(now.currentDate().shortMonthName(now.month(), now.MonthNameType.DateFormat))
        self.timeText.resize(len(self.timeText.text())*19+22, len(self.timeText.text())*112)
        self.timeText.setStyleSheet("font: bold; font-size:34px; color:white; font-family: 'Game of squids';")
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint, True)
        self.setWindowFlag(Qt.WindowType.WindowStaysOnBottomHint, True)
        self.setWindowFlag(Qt.WindowType.WindowTransparentForInput, True)

        print(now.currentDate().toString()) 
        print(str(QTime.currentTime().hour()) + ":" + str(QTime.currentTime().minute()) )
    @pyqtSlot()
    def open(self, url=QUrl(filename)):
        self._player.setMedia(QMediaContent(url))
        self._player.play()

    @pyqtSlot()
    def check_position(self):
        # Check if the video has reached its end
        if self._player.state() == QMediaPlayer.State.StoppedState:
            self._player.setPosition(0)  # Seek back to the beginning
            self._player.play()

    def show_status_message(self, message):
        self.statusBar().showMessage(message, 5000)

    @pyqtSlot("QMediaPlayer::Error", str)
    def _player_error(self, error, error_string):
        print(error_string, file=sys.stderr)
        self.show_status_message(error_string)

    def active(self):
        forground = win32gui.GetForegroundWindow()
        if forground == self.winId():
            taskbar = win32gui.FindWindow("Shell_TrayWnd", None)
            win32gui.SetFocus(taskbar)
            win32gui.ShowWindow(taskbar, win32con.SWP_SHOWWINDOW)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.showFullScreen()
    
    sys.exit(app.exec())
