import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QVBoxLayout, QMenuBar, QLabel, QAction, QFontDialog, QTextEdit, QColorDialog, QFileDialog, QMessageBox
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import Qt
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog, QPrintPreviewDialog
from PyQt5.QtCore import QFileInfo

class MainForm(QMainWindow) :
    def __init__(self) :
        super(MainForm, self).__init__()
        self.setWindowTitle("QFileInfo()")
        self.setWindowIcon(QIcon('icon.jpg'))
        self.setGeometry(200, 200, 500, 500)
        # self.setStyleSheet("background-color:yellow")
        self.initUI()
    
    def initUI(self) :
        # vbox = QVBoxLayout()

        mainmenu = self.menuBar()
        filemenu = mainmenu.addMenu("File")
        editmenu = mainmenu.addMenu("Edit")
        viewmenu = mainmenu.addMenu("Edit")
        helpmenu = mainmenu.addMenu("Help")

        
        pdfaction = QAction(QIcon(":/blue.ico"), "Export PDF", self)
        pdfaction.triggered.connect(self.pdfExport)
        filemenu.addAction(pdfaction)

        printaction = QAction(QIcon(":/blue.ico"), "Print", self)
        printaction.triggered.connect(self.printDialog)
        filemenu.addAction(printaction)

        printpreviewaction = QAction(QIcon(":/blue.ico"), "Print Preview", self)
        printpreviewaction.triggered.connect(self.printPreviewDialog)
        filemenu.addAction(printpreviewaction)

        copyaction = QAction(QIcon(":/blue.ico"), "Copy", self)
        copyaction.setShortcut("Ctrl + C")
        editmenu.addAction(copyaction)

        cutaction = QAction(QIcon(":/icons/icon.png"), "Cut", self)
        cutaction.setShortcut("Ctrl + X")
        editmenu.addAction(cutaction)

        saveaction = QAction(QIcon("./images/icons/blue.ico"), "Save", self)
        saveaction.setShortcut("Ctrl + S")
        editmenu.addAction(saveaction)

        exitaction = QAction(QIcon("close.ico"), "Exit", self)
        exitaction.setShortcut("Ctrl + E")
        exitaction.triggered.connect(self.exitWindow)
        filemenu.addAction(exitaction)

        fontaction = QAction(QIcon("close.ico"), "Font", self)
        fontaction.setShortcut("Ctrl + F")
        fontaction.triggered.connect(self.fontDialog)
        viewmenu.addAction(fontaction)

        coloraction = QAction(QIcon("close.ico"), "Color", self)
        coloraction.setShortcut("Ctrl + ")
        coloraction.triggered.connect(self.colorDialog)
        viewmenu.addAction(coloraction)

        helpaction = QAction(QIcon("./images/icons/blue.ico"), "About Application", self)
        helpaction.triggered.connect(self.aboutMessageBox)
        helpmenu.addAction(helpaction)

        choiceaction = QAction(QIcon("./images/icons/blue.ico"), "Choie Message", self)
        choiceaction.triggered.connect(self.choiceMessageBox)
        helpmenu.addAction(choiceaction)

        toolbar = self.addToolBar("toolbar")
        toolbar.addAction(copyaction)
        toolbar.addAction(cutaction)
        toolbar.addAction(saveaction)
        toolbar.addAction(exitaction)
        toolbar.addAction(fontaction)
        toolbar.addAction(coloraction)
        toolbar.addAction(printaction)
        toolbar.addAction(printpreviewaction)
        toolbar.addAction(pdfaction)
        toolbar.addAction(helpaction)

        self.textedit = QTextEdit()
        self.setCentralWidget(self.textedit)

        
        


        # self.setLayout(vbox)


    def exitWindow(self) :
        self.close()

    def fontDialog(self) :
        font, ok = QFontDialog.getFont()
        if ok :
            self.textedit.setFont(font)
         
    def colorDialog(self) :
        color = QColorDialog.getColor()
        self.textedit.setTextColor(color)
       
    def printDialog(self) :
        printer = QPrinter(QPrinter.HighResolution)
        dialog = QPrintDialog(printer, self)
        if dialog.exec_() == QPrintDialog.Accepted :
            self.textedit.print_(printer)
     
    def printPreviewDialog(self) :
        printer = QPrinter(QPrinter.HighResolution)
        previewdialog = QPrintPreviewDialog(printer, self)
        previewdialog.paintRequested.connect(self.printPreview)
        previewdialog.exec_()
     
    def printPreview(self, printer) :
        self.textedit.print_(printer)
              
    def pdfExport(self) :
        fn, _ = QFileDialog.getSaveFileName(self, "Export PDF", None, "PDF Files (.pdf);;All Files ()")
        if fn != "" :
            if QFileInfo(fn).suffix() == "" :fn += ".pdf" 
            printer = QPrinter(QPrinter.HighResolution)
            printer.setOutputFormat(QPrinter.PdfFormat)
            printer.setOutputFileName(fn)
            self.textedit.document().print_(printer)
        else :
            print("hataa")

    def aboutMessageBox(self) :
        message = QMessageBox.about(self,"About application","this is a simple application")

    def choiceMessageBox(self) :
        message = QMessageBox.question(self,"choice message","do you like pyqt5 ?", QMessageBox.Yes | QMessageBox.No)
        if message == QMessageBox.Yes :
            self.textedit.setText("Yes, I like pyqt5")
        else :
            self.textedit.setText("No, I do not like pyqt5")

            
        
       
  

def window() :
    app = QApplication(sys.argv)
    win = MainForm()
    win.show()
    sys.exit(app.exec_()) # x ile kapatılabilme

window()
