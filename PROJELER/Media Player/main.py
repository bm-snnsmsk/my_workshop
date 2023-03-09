from PyQt5.QtWidgets import QApplication, QWidget, QSlider, QHBoxLayout, QVBoxLayout, QPushButton, QLabel, QStyle, QSizePolicy, QFileDialog
import sys
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtGui import QIcon, QPalette
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget


class MainWindow(QWidget) :
    def __init__(self) :
        super().__init__()

        self.setWindowTitle("Media Player")
        self.setGeometry(350,100,700,500)
        self.setWindowIcon(QIcon("start.ico"))

        p = self.palette()
        p.setColor(QPalette.Window, Qt.black)
        self.setPalette(p)

        self.initUi()

    def initUi(self) :
        ## QMediaPlayer START
        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        ## QMediaPlayer END

        ## QVideoWidget START
        videowidget = QVideoWidget()
        ## QVideoWidget END

        ## openBtn START
        openBtn = QPushButton("Open Video")
        openBtn.clicked.connect(self.open_file)
        ## openBtn END

        ## playBtn START
        self.playBtn = QPushButton()
        self.playBtn.setEnabled(False)
        self.playBtn.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay)) ## standart play iconlu button oluşturur
        self.playBtn.clicked.connect(self.play_video)
        ## playBtn END

        ## QSlider START
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setRange(0,0)
        self.slider.sliderMoved.connect(self.set_position)
        ## QSlider END

        ## QLabel START
        self.label = QLabel()
        self.label.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        ## QLabel END

        ## QHBoxLayout START
        hbox = QHBoxLayout()
        hbox.setContentsMargins(0,0,0,0)
        hbox.addWidget(openBtn)
        hbox.addWidget(self.playBtn)
        hbox.addWidget(self.slider)        
        ## QHBoxLayout END

        ## QVBoxLayout START
        vbox = QVBoxLayout()
        vbox.addWidget(videowidget)
        vbox.addLayout(hbox)
        vbox.addWidget(self.label)        
        ## QVBoxLayout END

        self.setLayout(vbox)

        self.mediaPlayer.setVideoOutput(videowidget)
        self.mediaPlayer.stateChanged.connect(self.mediastate_changed)
        self.mediaPlayer.positionChanged.connect(self.position_changed)
        self.mediaPlayer.durationChanged.connect(self.duration_changed)

    def open_file(self) :
        filename, _ = QFileDialog.getOpenFileName(self, "Open Video", "" , "Media Files (*.mp4)")
        if filename != "" :
            self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(filename)))
            self.playBtn.setEnabled(True)
    
    def play_video(self) :
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState :
            self.mediaPlayer.pause()
        else :
            self.mediaPlayer.play()
    
    def mediastate_changed(self, state) :
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState :
            self.playBtn.setIcon(self.style().standardIcon(QStyle.SP_MediaPause))
        else :
            self.playBtn.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
    
    def position_changed(self, position) :
        self.slider.setValue(position)
    
    def duration_changed(self, duration) :
        self.slider.setRange(0, duration)
    
    def set_position(self, position) :
        self.mediaPlayer.setPosition(position)

    def handle_errors(self) :
        self.playBtn.setEnabled(False)
        self.label.setText("Error : "+ self.mediaPlayer.errorString())




        



def application() :
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())

application()