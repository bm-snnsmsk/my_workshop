from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sys
from messagebox import Ui_MainWindow



class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btn_exit.clicked.connect(self.show_dialog)

    def show_dialog(self) :
    #   show dialog penceresi KISAYOL START
        result = QMessageBox.question(self, "Kapatma Uygulaması", "Emin misin ?",QMessageBox.Ok | QMessageBox.Ignore | QMessageBox.Cancel, QMessageBox.Cancel)

        if result == QMessageBox.Ok :
            print("okey ...")
            QtWidgets.qApp.quit()
        else :
            print("no clicked...")
    #   show dialog penceresi KISAYOL END

    #   show dialog penceresi UZUN YOL START
    #     msg = QMessageBox()
    #     msg.setWindowTitle("Kapatma Uygulaması")
    #     msg.setText("Emin misin ?")
    #     #msg.setIcon(QMessageBox.Question)  
    #     msg.setIcon(QMessageBox.Warning) 
    #     msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Ignore | QMessageBox.Cancel) 
    #     msg.setDefaultButton(QMessageBox.Ok) ## varsayılan seçilmiş buton
    #     msg.setDetailedText("uygulama kapatılcak. kaydedilmemiş verileriniz kaybolabilir.") ## detay butonu
    #     msg.buttonClicked.connect(self.popup_button)

    #     x = msg.exec_()

    #     print(x)
    
    # def popup_button(self, i) :## i = tıklanan buton bilgisi self.sender() gibi
    #     print(i.text())

    #     if i.text() == 'OK' :
    #         print("Okey tuşuna bastınız")
    #         QtWidgets.qApp.quit()
    #     elif i.text() == 'Cancel' :
    #         print("Cancel Tuşuna Bastınız")
    #     elif i.text() == 'Ignore' :
    #         print("ignore tuşuna bastınız")
    #     else :
    #         print("diğer bir tuşa bastınız")

     #   show dialog penceresi UZUN YOL END

      

      


    

       


        
def app() :
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())  
    

app()


