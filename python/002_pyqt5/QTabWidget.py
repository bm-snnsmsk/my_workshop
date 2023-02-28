import sys
from PyQt5.QtWidgets import QDialog, QApplication, QGroupBox, QCheckBox, QComboBox, QTabWidget, QWidget, QVBoxLayout, QDialogButtonBox, QLabel, QLineEdit
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import Qt

class Tab(QDialog) :
    def __init__(self) :
        super().__init__()
        self.setWindowTitle("QTabWidget()")
        self.setWindowIcon(QIcon('icon.jpg'))
        self.setGeometry(200, 200, 300, 250)

        vbox = QVBoxLayout() 
        tabwidget = QTabWidget()

        buttonbox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttonbox.accepted.connect(self.accept)
        buttonbox.rejected.connect(self.rejected)

        tabwidget.addTab(TabContact(),"Contact Detail")
        tabwidget.addTab(TabPersonDetails(),"Personal Details")

        vbox.addWidget(tabwidget)
        vbox.addWidget(buttonbox)
        self.setLayout(vbox)


class TabContact(QWidget) :
    def __init__(self) :
        super().__init__()

        namelabel = QLabel("adınız : ")
        nameedit = QLineEdit()

        phonelabel = QLabel("telefon : ")
        phonedit = QLineEdit()

        emaillabel = QLabel("email : ")
        emailedit = QLineEdit()

        addrlabel = QLabel("adres : ")
        addredit = QLineEdit()

        vbox = QVBoxLayout()

        vbox.addWidget(namelabel)
        vbox.addWidget(nameedit)

        vbox.addWidget(phonelabel)
        vbox.addWidget(phonedit)

        vbox.addWidget(emaillabel)
        vbox.addWidget(emailedit)

        vbox.addWidget(addrlabel)
        vbox.addWidget(addredit)


        self.setLayout(vbox)


  
class TabPersonDetails(QWidget) :
    def __init__(self) :
        super().__init__()

        groupBox = QGroupBox("select your gender")
        list = ["male","female"]

        combo = QComboBox()
        combo.addItems(list)
        vbox = QVBoxLayout()
        vbox.addWidget(combo)
        groupBox.setLayout(vbox)

        

        groupBox2 = QGroupBox("select your gender favourite programin language" )
        python = QCheckBox("python")
        cpp = QCheckBox("c++")
        java = QCheckBox("java")
        csharp = QCheckBox("c#")
        vboxp = QVBoxLayout()
        vboxp.addWidget(python)
        vboxp.addWidget(cpp)
        vboxp.addWidget(java)
        vboxp.addWidget(csharp)
        groupBox2.setLayout(vboxp)

        mainlayout = QVBoxLayout()
        mainlayout.addWidget(groupBox)
        mainlayout.addWidget(groupBox2)

        self.setLayout(mainlayout)
        
        
        
      
       
  

def window() :
    app = QApplication(sys.argv)
    win = Tab()
    win.show()
    sys.exit(app.exec_()) # x ile kapatılabilme

window()
