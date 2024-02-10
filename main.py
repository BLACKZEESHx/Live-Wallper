# import module 
import sys, cv2, datetime, win32gui, win32con
from PyQt5.QtCore import Qt, pyqtSlot, QUrl, QTimer, QDate
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget, QWidget, QLabel
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
        # self.image = QPixmap(image_path)
        # self.timeText.setPixmap(self.image)
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
        now = QDate.currentDate()
        print("d", now.toString(Qt.DefaultLocaleLongDate))
        self.timeText = QLabel(self)
        image_path = "image.jpg"
        self.timeText.setStyleSheet("font: bold; font-size:34px; color:white; background-image: url('image.jpg'); background-repeat: no-repeat")
        self.timeText.setText(now.toString(Qt.DefaultLocaleLongDate))
        self.timeText.resize(len(self.timeText.text())*18+22, len(self.timeText.text())*2)
        self.save_first_frame(filename, image_path)
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint, True)
        self.setWindowFlag(Qt.WindowType.WindowStaysOnBottomHint, True)
        self.setWindowFlag(Qt.WindowType.WindowTransparentForInput, True)

    def save_first_frame(self, video_path, output_path):
        # Open the video file
        cap = cv2.VideoCapture(video_path)

        # Check if the video opened successfully
        if not cap.isOpened():
            print("Error: Could not open video.")
            return

        # Read the first frame
        ret, frame = cap.read()
        x, y = 860, 530  # Top-left corner
        width, height = self.timeText.geometry().width(), self.timeText.geometry().height()  # Width and height of the region
        # Crop the image from the top-left corner to the end
        crop = frame[y+y:height, x+x:width]
        # Crop the image using array slicing
        # crop = frame[:height, :width]

        # resizedFrame = cv2.resize(frame, (32, 22), interpolation=cv2.INTER_AREA)

        # Check if the frame was read successfully
        if not ret:
            print("Error: Could not read frame.")
            return

        # Save the first frame as an image
        cv2.imwrite(output_path, crop)
        print("First frame saved as", output_path)

        # Release the video capture object
        cap.release()
        # Load the image


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
