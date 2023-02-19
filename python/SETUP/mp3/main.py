import sys
import os

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
import qdarkgraystyle # koyu arkaplan

class MainWindow(QWidget) :
    def __init__(self):
        super().__init__() 
        self.init_ui()

        
        self.state = 'Play'
        self.playlist = []
        self.position = 0
        self.index = ''

        p = self.palette()
        color = QColor('#77ab9c')
        color.setAlpha(200)
        p.setColor(QPalette.Window, QColor(color))
        self.setPalette(p)


    def init_ui(self):
        vb = QVBoxLayout()
        self.setLayout(vb)
        vb.setAlignment(Qt.AlignCenter)

        self.label = QLabel("MP3 Player 2023")   
        self.label.setFont(QFont('Calibri', 22))     
        self.label.setAlignment(Qt.AlignCenter)     
        vb.addWidget(self.label)

        hb = QHBoxLayout()
        vb.addLayout(hb)

        font = QFont("Clibri",14)
        self.skipbackwardbtn = QPushButton()
        self.skipbackwardbtn.setIcon(self.style().standardIcon(QStyle.SP_MediaSkipBackward))
        hb.addWidget(self.skipbackwardbtn)
        self.backwardbtn = QPushButton()
        self.backwardbtn.setIcon(self.style().standardIcon(QStyle.SP_MediaSeekBackward)) ## standart geri iconu
        self.backwardbtn.setFont(font) 
        hb.addWidget(self.backwardbtn)
        self.playbtn = QPushButton("Play")
        # self.playbtn.setEnabled(False) # listede şarkı olduğundan bu satıra gerek yok
        self.playbtn.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))## standart play iconu
        self.playbtn.setFont(font)
        hb.addWidget(self.playbtn)
        self.forwardbtn = QPushButton()
        self.forwardbtn.setIcon(self.style().standardIcon(QStyle.SP_MediaSeekForward))## standart ileri iconu
        self.forwardbtn.setFont(font) 
        hb.addWidget(self.forwardbtn)
        self.skipforwardbtn = QPushButton()
        self.skipforwardbtn.setIcon(self.style().standardIcon(QStyle.SP_MediaSkipForward))
        hb.addWidget(self.skipforwardbtn)

        hb2 = QHBoxLayout()
        vb.addLayout(hb2)

        self.openfilebtn = QPushButton("Open")
        self.openfilebtn.setIcon(self.style().standardIcon(QStyle.SP_DirOpenIcon))## standart dosya iconu
        self.openfilebtn.setFont(font) 
        hb2.addWidget(self.openfilebtn)

        self.slider = QSlider(Qt.Horizontal)
        self.slider.setRange(0,0)
        self.slider.sliderMoved.connect(self.set_position)
        hb2.addWidget(self.slider)

        self.songlist = QListWidget()
        vb.addWidget(self.songlist)
          
        self.songlist.addItem(str("Burak Yeter - Tuesday ft. Danelle Sandoval.mp3"))
        self.songlist.addItem(str("J Balvin - Tranquila (1).mp3"))
        self.songlist.addItem(str("inna.mp3"))
        self.songlist.addItem(str("ahmet_aslan_beni_hor_görme.mp3"))
        self.songlist.addItem(str("cavbella.mp3"))
        self.songlist.addItem(str("ender_balkir_ruhumda_sizi.mp3"))
        self.songlist.setCurrentRow(0) # seçili eleman

        self.toolbar = QToolBar()
        vb.addWidget(self.toolbar)

        self.opefileaction = QAction()
        self.opefileaction.setIcon(self.style().standardIcon(QStyle.SP_DirOpenIcon))## standart dosya iconu
        self.opefileaction.setFont(font)
        self.opefileaction.triggered.connect(self.open_mp3_file)
        self.toolbar.addAction(self.opefileaction)
        self.toolbar.addSeparator() ## separator ekle
        self.toolbar.addSeparator() ## separator ekle
        self.toolbar.addSeparator() ## separator ekle
        self.toolbar.addSeparator() ## separator ekle

        self.player = QMediaPlayer() # mediaplayer tanımlaması
        # self.volumedown = QAction("-")
        # self.toolbar.addAction(self.volumedown)
        # self.volumedown.setFont(font)
        # self.volumeup = QAction("+")
        # self.toolbar.addAction(self.volumeup)
        # self.volumeup.setFont(font)
        self.space = QWidget()       # toolbar boşluk
        self.space.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)     
        self.toolbar.addWidget(self.space)       
        self.speaker = QAction()        
        self.speaker.setIcon(self.style().standardIcon(QStyle.SP_MediaVolume))   
        self.toolbar.addAction(self.speaker)  
        self.slider_vl = QSlider(Qt.Horizontal) # varsayılan Qt.Vertical
        self.toolbar.addWidget(self.slider_vl)   
        self.label_vl = QLabel("50%")
        self.label_vl.setFont(QFont('Helvetica', 10))
        self.label_vl.setMinimumWidth(40)
        self.toolbar.addWidget(self.label_vl)
        self.slider_vl.setRange(0,100)
        volume = self.player.volume()
        self.slider_vl.setValue(int(volume/2))


        self.openfilebtn.clicked.connect(self.open_mp3_file)
        self.playbtn.clicked.connect(self.play_mp3)
        self.player.positionChanged.connect(self.position_changed)
        self.player.durationChanged.connect(self.duration_changed)
        self.player.stateChanged.connect(self.state_changed)
        self.backwardbtn.clicked.connect(self.move_backward)
        self.forwardbtn.clicked.connect(self.move_forward)
        self.songlist.clicked.connect(self.set_state)
        self.songlist.doubleClicked.connect(self.play_mp3)
        self.skipbackwardbtn.clicked.connect(self.skip_backward)
        self.skipforwardbtn.clicked.connect(self.skip_forward)
        self.slider_vl.valueChanged.connect(self.set_volume)


    def open_mp3_file(self) :
        file_name = QFileDialog()
        file_name.setFileMode(QFileDialog.ExistingFiles)
        file_name.getOpenFileName(self, tr("Open File"),"/home",tr("Images (*.png *.xpm *.jpg)"))
        ##file_name.setDirectoryUrl(QUrl('C:\Users\bm_snnsmsk\Desktop\my_workspace\python\music'))
        print(str(file_name.directoryUrl()))
        names = file_name.getOpenFileNames(self,"Müzik Aç", os.getenv('HOME'))
        self.song = names[0]
        sarki_listesi = []
        for i in range(0,len(self.song)) :
            bol = self.song[i].split('/')
            #print(bol[len(bol) - 1])   
            sarki_listesi.append(bol[len(bol) - 1])
        self.songlist.addItems(sarki_listesi)
        # self.songlist.addItems(self.song)
       

    def play_mp3(self) :
        if self.state == 'Play' :
            self.playbtn.setText('Pause')
            self.state = 'Pause'
            path = self.songlist.currentItem().text()
            url = QUrl.fromLocalFile(path)
            content = QMediaContent(url)        
            self.player.setMedia(content)
            self.index = self.songlist.currentRow().__index__()
            self.player.setPosition(self.position) # musiğin geçerli durumu
            self.playlist.append(path)
            if len(self.playlist) > 2 :
                self.playlist.pop(0) 
            if self.songlist.currentItem().text() != self.playlist[0] :
                self.position = 0
                self.player.setPosition(self.position)
            self.player.play()
        else :
            self.playbtn.setText('Play')
            self.state = 'Play'
            self.player.pause()
            paused = self.player.position()
            self.position = paused
    
    def set_position(self, position) :
        self.player.setPosition(position)
    
    def position_changed(self, position) :
        self.slider.setValue(position)
        duration = self.player.duration()
        value = self.slider.value()
        if value == duration :
            #self.skip_forward()
            self.state = 'Play'
            self.play_mp3() # şarkı tekrar tekrar çalınır
    
    def duration_changed(self, duration) :
        self.slider.setRange(0, duration)
    
    def state_changed(self, state) :
        if self.player.state() == QMediaPlayer.PlayingState :
            self.playbtn.setIcon(self.style().standardIcon(QStyle.SP_MediaPause))
        else :
            self.playbtn.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))

    def move_forward(self) :
        self.player.setPosition(int(self.player.position()) + 2000)

    def move_backward(self) :
        self.player.setPosition(int(self.player.position()) - 2000)

    def set_state(self) :
        self.playbtn.setEnabled(True)
        self.state = 'Play'
        self.playbtn.setText('Play')
        self.playbtn.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))

    def skip_backward(self) :
        self.state = 'Play'
        try : # liste eleman sayısı aşımında hata vermemesi için
            self.songlist.setCurrentRow(self.index - 1)
            self.play_mp3()
        except : # liste eleman sayısı aşımında hata vermemesi için
            pass

    def skip_forward(self) :
        self.state = 'Play'
        try : # liste eleman sayısı aşımında hata vermemesi için
            self.songlist.setCurrentRow(self.index + 1)
            self.play_mp3()
        except : # liste eleman sayısı aşımında hata vermemesi için
            pass

    
    def set_volume(self) :
        volume = self.slider_vl.value()
        self.player.setVolume(volume)
        self.label_vl.setText(str(volume)+ "%")
        

def main() :
    app = QApplication(sys.argv)
    #app.setStyleSheet(qdarkgraystyle.load_stylesheet()) #  koyu arkaplan
    gui = MainWindow()
    gui.setWindowTitle("MP3 Player 0.1 (2023)")
    gui.setWindowIcon(QIcon('mp3.ico'))
    gui.setGeometry(300,300,600,700)
    gui.show()
    sys.exit(app.exec_())

if __name__ == '__main__' :
    main()
