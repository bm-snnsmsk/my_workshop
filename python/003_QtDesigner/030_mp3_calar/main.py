from PyQt5 import QtWidgets
import sys, os
from untitled import Ui_MainWindow

from PyQt5.QtCore import QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent



class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton_play.clicked.connect(self.play_audio_file)
        self.ui.pushButton_eksi.clicked.connect(self.volume_down)
        self.ui.pushButton_arti.clicked.connect(self.volume_up)
        self.ui.pushButton_pause.clicked.connect(self.play_audio_pause)
        self.ui.pushButton_mute.clicked.connect(self.volume_mute)
        self.ui.pushButton_stop.clicked.connect(self.play_audio_stop)
        

        self.player = QMediaPlayer()
        self.current_volume = self.player.volume()

        self.player.durationChanged.connect(self.calisiyor)
        
        

    def calisiyor(self) :  
        self.ui.label_sure.setText(str(self.player.duration()))  

    def volume_up(self) :        
        print(str(self.current_volume) + ' - ' + str(self.player.duration()))
        self.player.setVolume(self.current_volume + 5)  

    def volume_down(self) :
        print(str(self.current_volume) + ' - ' + str(self.player.duration()))
        self.player.setVolume(self.current_volume - 5)

    def volume_mute(self) :
        print(self.player.duration())
        self.player.setMuted(not self.player.isMuted())

    def play_audio_pause(self) :
        self.player.pause()

    def play_audio_stop(self) :
        self.player.stop()

    def play_audio_file(self) :
        ## full_file_path = os.path.join(os.getcwd(), 'ender_balkir_ruhumda_sizi.mp3')
        full_file_path = os.path.join(os.getcwd(), 'cavbella.mp3')
        # full_file_path = os.path.join(os.getcwd(), 'ahmet_aslan_beni_hor_görme.mp3')
        url = QUrl.fromLocalFile(full_file_path)
        content = QMediaContent(url)
        self.ui.label_sure.setText(str(self.player.duration()))       
        self.player.setMedia(content)
        self.player.play()
        #self.ui.label_sure.setText(str(self.player.duration())) 


       

 


        


    

  

      
        
def app() :
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())  
    

app()


