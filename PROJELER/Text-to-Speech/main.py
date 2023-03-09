import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtTextToSpeech import QTextToSpeech

from untitled import Ui_MainWindow


class Mainwindow(QMainWindow) :
    def __init__(self) :
        super().__init__() 
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.engine = None

        engineNames = QTextToSpeech.availableEngines()

        self.ui.pushButton.clicked.connect(self.say)

        if len(engineNames) > 0 :
            engineName = engineNames[0]
            self.engine = QTextToSpeech(engineName)
            self.engine.stateChanged.connect(self.stateChanged)

            self.voices = []
            for voice in self.engine.availableVoices() :
                self.voices.append(voice)
                self.ui.comboBox.addItem(voice.name())
        else :
            self.ui.pushButton.setEnabled(False)

    
    def stateChanged(self, state) :
        if state == QTextToSpeech.State.Ready :
            self.ui.pushButton.setEnabled(True)

    def say(self) : ## benim fonksiyonum
        self.ui.pushButton.setEnabled(False)
        self.engine.setVoice(self.voices[self.ui.comboBox.currentIndex()])
        self.engine.setVolume(float(self.ui.horizontalSlider.value() / 100))
        self.engine.say(self.ui.lineEdit.text()) ## engine say() fonksiyonu
















def application() :
    app = QApplication(sys.argv)
    win = Mainwindow()
    win.show()
    sys.exit(app.exec_())

application()



