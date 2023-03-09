import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon, QPainter
from PyQt5.QtCore import Qt
from PyQt5.QtChart import QChart, QChartView, QBarSet, QBarCategoryAxis, QPercentBarSeries
## pip install PyQtChart

class MainWindow(QMainWindow) :
    def __init__(self) :
        super().__init__()
        self.setWindowTitle("QChart()")
        self.setWindowIcon(QIcon('icon.jpg'))
        self.setGeometry(200, 200, 800, 600)        
        self.initUI()

    def initUI(self) :


        ## chart START
        set_0 = QBarSet("emine")
        set_1 = QBarSet("tubanur")
        set_2 = QBarSet("baran")
        set_3 = QBarSet("sinan")
        set_4 = QBarSet("pelçim")

        set_0 << 1 << 2 << 3 << 4 << 5 << 6
        set_1 << 5 << 0 << 0 << 4 << 0 << 7
        set_2 << 3 << 5 << 8 << 13 << 8 << 5
        set_3 << 5 << 6 << 7 << 3 << 4 << 5
        set_4 << 9 << 7 << 5 << 3 << 1 << 2

        series = QPercentBarSeries()
        series.append(set_0)
        series.append(set_1)
        series.append(set_2)
        series.append(set_3)
        series.append(set_4)

        chart = QChart()
        chart.addSeries(series)
        chart.setTitle("Percent BarChart Example")
        chart.setAnimationOptions(QChart.SeriesAnimations)

        categories = ["Jan","Feb","Mar","Apr","May","Jun"]
        axis = QBarCategoryAxis()
        axis.append(categories)
        chart.createDefaultAxes()
        chart.setAxisX(axis, series)

        ## set isimleri konumu START    
        chart.legend().setVisible(True)
        chart.legend().setAlignment(Qt.AlignBottom)
        ## set isimleri konumu END

        chartview = QChartView(chart)
        chartview.setRenderHint(QPainter.Antialiasing)

        self.setCentralWidget(chartview)
        ## chart END


    


def window() :
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_()) # x ile kapatılabilme

window()
