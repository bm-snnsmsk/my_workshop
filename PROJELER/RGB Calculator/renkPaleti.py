from renk_paleti import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow


class MainWindow(QMainWindow) :
    def __init__(self) :
        super().__init__() 
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.red = "0"
        self.blue = "0"
        self.green = "0"

        self.ui.horizontalSlider_red.valueChanged.connect(self.red_value)
        self.ui.horizontalSlider_green.valueChanged.connect(self.green_value)
        self.ui.horizontalSlider_blue.valueChanged.connect(self.blue_value)

    def red_value(self) :        
        self.red = self.ui.horizontalSlider_red.value()
        self.ui.label_red.setText(str(self.red))
        self.ui.label_rgb.setText(f"rgb({self.red}, {self.blue}, {self.green})")
        self.ui.label_renk_alani.setStyleSheet(f"background-color:rgb({self.red}, {self.blue}, {self.green})")
        
    def green_value(self) :        
        self.green = self.ui.horizontalSlider_green.value()
        self.ui.label_green.setText(str(self.green))
        self.ui.label_rgb.setText(f"rgb({self.red}, {self.blue}, {self.green})")
        self.ui.label_renk_alani.setStyleSheet(f"background-color:rgb({self.red}, {self.blue}, {self.green})")
        
    def blue_value(self) :        
        self.blue = self.ui.horizontalSlider_blue.value()
        self.ui.label_blue.setText(str(self.blue))
        self.ui.label_rgb.setText(f"rgb({self.red}, {self.blue}, {self.green})")
        self.ui.label_renk_alani.setStyleSheet(f"background-color:rgb({self.red}, {self.blue}, {self.green})")
        




