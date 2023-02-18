from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sys
from qmessagebox import Ui_MainWindow



class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton_critical.clicked.connect(self.critical_slot)
        self.ui.pushButton_information.clicked.connect(self.information_slot)
        self.ui.pushButton_about.clicked.connect(self.about_slot)
        self.ui.pushButton_numbers.clicked.connect(self.numbers_slot)
        self.ui.pushButton_qt.clicked.connect(self.qt_slot)
        self.ui.pushButton_question.clicked.connect(self.question_slot)
        self.ui.pushButton_warning.clicked.connect(self.warning_slot)

    # ------------------------------------------------------------
    def critical_slot(self) :
        #QMessageBox.critical(self, "Kritik mesaj","Bu bir kritik mesajdır")
        result = QMessageBox.critical(self, "Kritik mesaj","Bu bir kritik mesajdır",QMessageBox.Yes | QMessageBox.No) ## varsayılan iconlar sadece QMessageBox.Ok 
        if result == QMessageBox.Yes : 
            print("kullanıcı evet dedi = > "+str(result))
        elif result == QMessageBox.No:
            print("kulanıcı hayır dedi => "+str(result))
        else :
            print("farklı bir seçenek =>"+str(result))


    # ------------------------------------------------------------
    def information_slot(self) :
        result = QMessageBox.information(self, "Bilgilendirme mesajı","Bu bir bilgilendirme mesajıdır",QMessageBox.Yes | QMessageBox.No) ## varsayılan iconlar sadece QMessageBox.Ok
        if result == QMessageBox.Yes : 
            print("kullanıcı evet dedi = > "+str(result))
        elif result == QMessageBox.No:
            print("kulanıcı hayır dedi => "+str(result))
        else :
            print("farklı bir seçenek =>"+str(result))

    # ------------------------------------------------------------
    def about_slot(self) :
        QMessageBox.about(self, "Hakkında","Bu dersler python ile arayüz çalışmalarından oluşmaktadır.<br/>Ayrıca <b>HTML</b> ile şekillendirilenebilmektedir.<br/><h2 style='color:red'>Örnek h2 başlığı</h2><a href='https://google.com'>Google</a>'a git..."
        "<br/>"
        "<b>İletişim : </b>"
        "<br/>"
        "<b>"
        "<a href='mailto:eemsinan.73@gmail.com'>eemsinan.73@gmail.com</a>"
        "</b>"
        )

    # ------------------------------------------------------------
    def numbers_slot(self) :  ## bu şekilde uzun yazılmasının sebebi buton isimlerini istediğimiz ismi verebilmemizdendir
        msg_box = QMessageBox(self) ## self yazılmazsa varsayılan ikon görünür
        msg_box.setWindowTitle("Özel Kullanım (Uzun yol)")
        msg_box.setText("Hangi sayıları kullanmak istiyorsunuz ?") 
        msg_box.setIcon(QMessageBox.Question) 
        msg_box.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel) 
        msg_box.setDefaultButton(QMessageBox.Ok) 
        msg_box.setEscapeButton(QMessageBox.Ok)  ##kullanıcı X ' a bassa .Ok çalışmış olacak

        btn_yes = msg_box.button(QMessageBox.Ok)
        btn_yes.setText("Tek Sayılar")

        btn_no = msg_box.button(QMessageBox.Cancel)
        btn_no.setText("Çift Sayılar")

        result = msg_box.exec_()

        ## print("result : "+ str(result))

        stop = 50
        step = 2
        start = 2

        if result == QMessageBox.Ok :
            start = 1
        elif result == QMessageBox.Cancel :
            start = 0
        
        self.ui.comboBox_numbers.clear() # her defasında combobox'ı silmek için, üzerine üzerine ekleme yapılmasın diye
        for i in range(start, stop, step) :
            self.ui.comboBox_numbers.addItem(str(i))

    # ------------------------------------------------------------
    def qt_slot(self) :
        QMessageBox.aboutQt(self, "Qt Hakkında")

    # ------------------------------------------------------------
    def question_slot(self) :
        #result = QMessageBox.question(self, "Soru mesajı","Bu bir soru sorma mesajdır")## varsayılan iconlar QMessageBox.Yes ve QMessageBox.No dır
        result = QMessageBox.question(self, "Soru mesajı","Bu bir soru sorma mesajdır",QMessageBox.Yes | QMessageBox.No | QMessageBox.Ok | QMessageBox.Open | QMessageBox.Save)
        if result == QMessageBox.Yes : 
            print("kullanıcı evet dedi = > "+str(result))
        elif result == QMessageBox.No:
            print("kulanıcı hayır dedi => "+str(result))
        else :
            print("farklı bir seçenek =>"+str(result))

    # ------------------------------------------------------------
    def warning_slot(self) :
        result = QMessageBox.warning(self, "Soru mesajı","Bu bir soru sorma mesajdır")## varsayılan iconlar sadece QMessageBox.Ok
        if result == QMessageBox.Yes : 
            print("kullanıcı evet dedi = > "+str(result))
        elif result == QMessageBox.No:
            print("kulanıcı hayır dedi => "+str(result))
        else :
            print("farklı bir seçenek =>"+str(result))


        
def app() :
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())  
    

app()


