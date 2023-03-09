import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon, QPainter, QPen
from PyQt5.QtCore import Qt
from PyQt5.QtChart import QChart, QChartView, QPieSeries, QPieSlice
## pip install PyQtChart

class MainWindow(QMainWindow) :
    def __init__(self) :
        super().__init__()
        self.setWindowTitle("QLineSeries()")
        self.setGeometry(200, 200, 800, 600)        
        self.setWindowIcon(QIcon('green.ico'))
        self.initUI()

    def initUI(self) :


        ## QPieSeries START
        series = QPieSeries()
        series.append("Python", 80)
        series.append("C++", 70)
        series.append("Java", 50)
        series.append("PHP", 80)
        series.append("JavaScript", 30)

        chart = QChart()
        chart.addSeries(series)
        chart.setAnimationOptions(QChart.SeriesAnimations)
        chart.setTitle("Programming Pie Chart Example")

        chart.legend().setVisible(True)
        chart.legend().setAlignment(Qt.AlignBottom)

        ## QPieSlice (dilim ekleme) START
            ## temel slice kodları START
        slice = QPieSlice() 
        slice = series.slices()[4]   ## hangi dilim öne çıkarılmak isteniyorsa indis numarası yazılır
        slice.setExploded(True)
            ## temel slice kodları END

            ## ek slice çizimleri START
        slice.setLabelVisible(True)   ## slice adı görünsün
        slice.setPen(QPen(Qt.darkRed, 5)) ## slice'ın etrafı çizilsin
        slice.setBrush(Qt.yellow) ## slice'ın içi doldurulsun
            ## ek slice çizimleri END
        ## QPieSlice (dilim ekleme) END

         ## QPieSlice (dilim ekleme) START
            ## temel slice kodları START
        slice2 = QPieSlice() 
        slice2 = series.slices()[2]   ## hangi dilim öne çıkarılmak isteniyorsa indis numarası yazılır
        slice2.setExploded(True)
            ## temel slice kodları END

            ## ek slice çizimleri START
        slice2.setLabelVisible(True)   ## slice adı görünsün
        slice2.setPen(QPen(Qt.darkBlue, 5)) ## slice'ın etrafı çizilsin
        slice2.setBrush(Qt.yellow) ## slice'ın içi doldurulsun
            ## ek slice çizimleri END
        ## QPieSlice (dilim ekleme) END

        chartview = QChartView(chart)
        chartview.setRenderHint(QPainter.Antialiasing)

        self.setCentralWidget(chartview)
        ## QPieSeries END


    


def window() :
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_()) # x ile kapatılabilme

window()
