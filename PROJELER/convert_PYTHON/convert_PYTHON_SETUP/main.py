from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox
import sys, os, subprocess
from PyQt5 import uic
from untitled import Ui_MainWindow

class MainWindow(QMainWindow) :
    def __init__(self) :
        super(MainWindow, self).__init__() 
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)        
        self.setWindowTitle("Convert 1.0")

        ### global definitions START
        self.file_path = ""        
        self.is_file_path = False 
        ### global definitions END

        ### ui to py definitions START
        self.ui.lineEdit_ui_to_py_file_name.editingFinished.connect(self.ui_to_py_py_filename)
        self.ui.lineEdit_ui_to_py_file_name.setFocus(True)
        self.ui.pushButton_ui_to_py_file_path.clicked.connect(self.select_ui_file_path)
        self.ui.pushButton_ui_to_py.clicked.connect(self.convert_ui_to_py)        
        self.ui_to_py_py_file_name = ""
        self.ui_to_py_ui_file_name = ""
        self.ui_to_py_ui_file_extension_name = ""
        ### ui to py definitions END 

        ### qrc to py definitions START
        self.ui.pushButton_qrc_to_py_file_path.clicked.connect(self.select_qrc_file_path)
        self.ui.pushButton_qrc_to_py.clicked.connect(self.convert_qrc_to_py)
        self.ui.lineEdit_qrc_to_py_file_path.setFocus(True)
        self.qrc_to_py_qrc_file_name = ""
        self.qrc_to_py_qrc_file_extension_name = ""
        ### qrc to py definitions END

        ### py to exe definitions START
        self.ui.pushButton_py_to_exe_folder_path.clicked.connect(self.select_py_to_exe_folder_path)
        self.ui.pushButton_py_to_exe_py_path.clicked.connect(self.select_py_to_exe_py_path)
        self.ui.pushButton_py_to_exe_icon_path.clicked.connect(self.select_py_to_exe_icon_path)
        self.ui.pushButton_py_to_exe.clicked.connect(self.convert_py_to_exe)        
        self.py_to_exe_icon_img_file_name = ""
        self.py_to_exe_icon_py_file_name = ""
        self.py_to_exe_icon_py_file_path = ""
        self.py_to_exe_folder_path = ""
        self.is_folder_path = False
        self.is_py_path = False
        ### py to exe definitions END

    ### ui to py functions START
    def init_ui_to_py(self) :
        self.is_file_path = False
        self.ui.lineEdit_ui_to_py_file_name.setFocus(True)
        self.ui.lineEdit_ui_to_py_file_name.setText("untitled.py")
        self.ui.lineEdit_ui_to_py_file_path.setText("")

    def ui_to_py_py_filename(self) :
        self.ui_to_py_py_file_name = self.ui.lineEdit_ui_to_py_file_name.text()
        if not self.ui_to_py_py_file_name.endswith(".py") :
            self.ui_to_py_py_file_name += ".py"

    def select_ui_file_path(self) :
        options = QFileDialog.Options()
        #filepath = QFileDialog.getOpenFileName(self, "ui Dosyası Seç", "", "All Files (*) ;;Design Dosyası (*.ui)", options=options)
        filepath, _ = QFileDialog.getOpenFileName(self, "ui Dosyası Seç", "", "Design Dosyası (*.ui)", options=options) ## sadece dosya full yolu, ayrıca popup tek seçenek
        if filepath :
            self.ui_to_py_ui_file_name = os.path.basename(filepath)
            self.file_path = os.path.dirname(filepath)
            self.ui_to_py_ui_file_extension_name = os.path.splitext(filepath)
            self.ui.lineEdit_ui_to_py_file_path.setText(self.ui_to_py_ui_file_name)
            self.ui.lineEdit_ui_to_py_file_name.setText(self.ui_to_py_ui_file_name[0:-3]+".py")
            self.is_file_path = True


    def convert_ui_to_py(self) :
        if self.is_file_path == True :
            if self.ui_to_py_ui_file_extension_name[1] != ".ui" :
                QMessageBox.critical(self, "Converter Mesajı", "Lütfen bir design(.ui) dosyası seçiniz")
            else :
                try :
                    with open(self.file_path+"/"+self.ui_to_py_py_file_name,"w",encoding="utf-8") as file :
                        uic.compileUi(self.file_path+"/"+self.ui_to_py_ui_file_name, file)
                    QMessageBox.information(self, "Converter Mesajı", f"{self.ui_to_py_ui_file_name} dosyası, {self.ui_to_py_py_file_name} dosyasına başarılı bir şekilde dönüştürülmüştür.")   
                    self.init_ui_to_py()                 
                except :
                    QMessageBox.critical(self, "Converter Mesajı", "Dönüştürme sırasında beklenmedik bir hata meydana geldi.")
        else :
            QMessageBox.critical(self, "Converter Mesajı", "Lütfen bir design(.ui) dosyası seçiniz")
    ### ui to py functions END

    ### qrc to py functions START
    def init_qrc_to_py(self) :
        self.is_file_path = False
        self.ui.lineEdit_qrc_to_py_file_path.setText("")
        self.ui.lineEdit_qrc_to_py_file_path.setFocus(True)

    def select_qrc_file_path(self) :
        options = QFileDialog.Options()
        filepath, _ = QFileDialog.getOpenFileName(self, "qrc Dosyası Seç", "", "Resource Dosyası (*.qrc)", options=options) 
        if filepath :
            self.qrc_to_py_qrc_file_name = os.path.basename(filepath)
            self.file_path = os.path.dirname(filepath)
            self.qrc_to_py_qrc_file_extension_name = os.path.splitext(filepath)
            self.ui.lineEdit_qrc_to_py_file_path.setText(self.qrc_to_py_qrc_file_name)
            self.is_file_path = True
    
    def convert_qrc_to_py(self) :        
        if self.is_file_path == True :
            if self.qrc_to_py_qrc_file_extension_name[1] != ".qrc" :
                QMessageBox.critical(self, "Converter Mesajı", "Lütfen bir resource(.qrc) dosyası seçiniz")
            else :
                try :
                    qrc_file_path = self.file_path + "/" + self.qrc_to_py_qrc_file_name
                    py_file_path = self.file_path + "/" + self.qrc_to_py_qrc_file_name[0:len(self.qrc_to_py_qrc_file_name) - 4] + "_rc.py"   
                    py_file_name = py_file_path.split("/")[-1]                
                    cmd_code = f"pyrcc5 {qrc_file_path} -o {py_file_path}"
                    subprocess.getoutput(cmd_code)
                    QMessageBox.information(self, "Converter Mesajı", f"{self.qrc_to_py_qrc_file_name} dosyası, {py_file_name} dosyasına başarılı bir şekilde dönüştürülmüştür.")
                    self.init_qrc_to_py()
                except :
                    QMessageBox.critical(self, "Converter Mesajı", "Dönüştürme sırasında beklenmedik bir hata meydana geldi.")
                    self.init_qrc_to_py()
        else :
            QMessageBox.critical(self, "Converter Mesajı", "Lütfen bir resource(.qrc) dosyası seçiniz")
    ### qrc to py functions END

    ### py to exe functions START
    def init_py_to_exe(self) :
        self.is_file_path = False
        self.is_folder_path = False
        self.is_py_path = False
        self.file_path = ""
        self.py_to_exe_icon_file_name = ""
        self.py_to_exe_py_file_name = ""
        self.py_to_exe_py_file_path = ""
        self.py_to_exe_folder_path = ""

    def select_py_to_exe_folder_path(self) :
        options = QFileDialog.Options()
        filepath = QFileDialog.getExistingDirectory(self, "Klasör Yolu Seç", "", options=options) 
        if filepath :
           self.py_to_exe_folder_path = filepath
           self.ui.lineEdit_py_to_exe_folder_path.setText(self.py_to_exe_folder_path.split("/")[-1])
           self.is_folder_path = True
    
    def select_py_to_exe_py_path(self) :
        options = QFileDialog.Options()
        filepath, _ = QFileDialog.getOpenFileName(self, "Python Dosyası", "", "Python Dosyası (*.py)", options=options) 
        if filepath :
            self.py_to_exe_py_file_name = os.path.basename(filepath)
            self.py_to_exe_py_file_path = os.path.dirname(filepath)
            self.ui.lineEdit_py_to_exe_py_path.setText(self.py_to_exe_py_file_name)
            self.is_py_path = True

    def select_py_to_exe_icon_path(self) :
        options = QFileDialog.Options()
        filepath, _ = QFileDialog.getOpenFileName(self, "Resim Dosyası", "", "Resim Dosyası (*.ico *.png *.jpg *.jpeg *.webp)", options=options) 
        if filepath :
            self.py_to_exe_icon_file_name = os.path.basename(filepath)
            self.file_path = os.path.dirname(filepath)
            self.ui.lineEdit_py_to_exe_icon_path.setText(self.py_to_exe_icon_file_name)
            self.is_file_path = True
    
    def convert_py_to_exe(self) :        
        if self.is_file_path == True and self.is_folder_path == True and self.is_py_path == True :
            try :
                py_file_path = self.py_to_exe_folder_path + "/" + self.py_to_exe_py_file_name
                img_file_path = self.file_path + "/" + self.py_to_exe_icon_file_name
                ###  "pyinstaller --onefile -w -i converter.png main.py"           
                cmd_code = f"pyinstaller --onefile -w -i {img_file_path} {py_file_path}"
                subprocess.getoutput(cmd_code)
                QMessageBox.information(self, "Converter Mesajı", f"{self.self.py_to_exe_py_file_name} dosyası, .exe dosyasına başarılı bir şekilde dönüştürülmüştür.")
                self.init_py_to_exe()
            except :
                QMessageBox.critical(self, "Converter Mesajı", "Dönüştürme sırasında beklenmedik bir hata meydana geldi.")
                self.init_py_to_exe()
        else :
            QMessageBox.critical(self, "Converter Mesajı", "Lütfen bir resim(.ico, .jpg, .jpeg, .webp, .png vb.) dosyası seçiniz")
    ### py to exe functions END

    









def app() :
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())

app()

        



