import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon, QPainter, QPen
from PyQt5.QtCore import Qt
from PyQt5.QtChart import QChart, QChartView, QPieSeries, QPieSlice
## pip install PyQtChart

class MainWindow(QMainWindow) :
    def __init__(self) :
        super().__init__()
        self.setWindowTitle("Donut Chart")
        self.setGeometry(200, 200, 800, 600)        
        self.setWindowIcon(QIcon('green.ico'))
        self.initUI()

    def initUI(self) :


        ## QPieSeries START
        series = QPieSeries()
        series.setHoleSize(0.35)

        series.append("Protein 4.28%", 4.28)
        slice = QPieSlice() 
        slice = series.append("Fat 15.6%", 15.6)
        slice.setExploded()
        slice.setLabelVisible() ## bu satır olmadan da çalışıyor

        series.append("Other 23.8%", 23.8)
        series.append("Carbs 56.4%", 56.4)

        chart = QChart()
        chart.addSeries(series)
        chart.setAnimationOptions(QChart.SeriesAnimations)
        chart.setTitle("Donut Chart Example")                 
        chart.setTheme(QChart.ChartThemeBlueCerulean)     ## tema             

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
