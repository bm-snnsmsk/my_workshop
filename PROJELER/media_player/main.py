import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QStyle, QSlider, QFileDialog
from PyQt5.QtGui import QIcon, QPalette
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtCore import Qt, QUrl


class MainWindow(QWidget) :
    
    def __init__(self) :
        super().__init__()
        self.setGeometry(350,100,700,500)
        self.setWindowTitle("Meadia Player")
        self.setWindowIcon(QIcon("reload.ico"))

        p = self.palette()
        p.setColor(QPalette.Window, Qt.red)
        self.setPalette(p)

        self.initUi()

    def initUi(self) :
        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)

        videowidget = QVideoWidget()

        self.openBtn = QPushButton("Open Video")
        self.openBtn.clicked.connect(self.open_file)

        self.playBtn = QPushButton()
        self.playBtn.setEnabled(False)
        self.playBtn.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.playBtn.clicked.connect(self.play_video)
        
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setRange(0,0)
        self.slider.sliderMoved.connect(self.set_position)
        
        hbox = QHBoxLayout()
        hbox.setContentsMargins(0,0,0,0)
        hbox.addWidget(self.openBtn)
        hbox.addWidget(self.playBtn)
        hbox.addWidget(self.slider)

        vbox = QVBoxLayout()
        vbox.addWidget(videowidget)

        vbox.addLayout(hbox)

        self.mediaPlayer.setVideoOutput(videowidget)

        self.setLayout(vbox)
    
        self.mediaPlayer.stateChanged.connect(self.mediastate_changed)
        self.mediaPlayer.positionChanged.connect(self.position_changed)
        self.mediaPlayer.durationChanged.connect(self.duration_changed)

    def open_file(self) :
        filename, _ = QFileDialog.getOpenFileName(self, "Open Video")
        if filename != "" :
            self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(filename)))#### !
            self.playBtn.setEnabled(True)

    def play_video(self) :
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState :
            self.mediaPlayer.pause()
        else :
            self.mediaPlayer.play() 
            ## codec i,ndirildikten sonra çalışmaya başladı
            ## https://codecguide.com/download_k-lite_codec_pack_standard.htm 

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
            
            
        






        


    


def applicaion() :
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())

applicaion()