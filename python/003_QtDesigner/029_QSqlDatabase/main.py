import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem, QMessageBox, QFileDialog
import pandas as pd
import mysql.connector as conn
from datetime import datetime


from qsqldatabase import Ui_MainWindow


class ConnectToMySQL() :
    def __init__(self) :
        self.host = "localhost"
        self.user = "root"
        self.password = ""
        #self.port = "3306"
        self.database_name = "abc-python"
        self.connDB = None

    def connectDB(self) :
        self.connDB = conn.connect(
            host=self.host,
            user=self.user,
            passwd=self.password,
            #port=self.port,
            database=self.database_name
        )

    def get_all_data_from_db(self) :
        try :
            self.connectDB()
            curs = self.connDB.cursor(dictionary=True)
            sql = "SELECT * FROM deneme"
            curs.execute(sql)
            result = curs.fetchall()
            return result
        except Exception as e :
            print("get data fail")
            print(e)
        finally :
            if self.connDB :
                self.connDB.close()

        


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        ## ======================================================
        ## init all widgets
        self.ui.pushButton_get_data.clicked.connect(self.get_data)
        self.ui.pushButton_get_path.clicked.connect(self.select_path)
        self.ui.pushButton_save_data.clicked.connect(self.save_data)
        self.file_path = self.ui.lineEdit
        self.result_table = self.ui.tableWidget

        

    ## ======================================================
    ## create functions
    def get_data(self) :
        print("get_datas fonksiyonu çalıştı")
        ## ======================================================
        ## get all the data from database
        result = ConnectToMySQL().get_all_data_from_db()
        if result :
            self.result_table.setRowCount(len(result))
            for row, item in enumerate(result) :
                column_1_item = QTableWidgetItem(str(item['denemeName']))
                column_2_item = QTableWidgetItem(str(item['denemeSurname']))

                self.result_table.setItem(row, 0, column_1_item)
                self.result_table.setItem(row, 1, column_2_item)
        else :
            ## ======================================================
            ## show message if no data got from database
            QMessageBox.information(self,"Warning","No data got from database, please try again !")
            return

            
    def select_path(self) :
        print("select_path fonksiyonu çalıştı")
        ## ======================================================
        ## get save file path
        folder_path = QFileDialog.getExistingDirectory(self, 'Select Folder')
        if folder_path :
            self.file_path.setText(folder_path)
        

    

    def save_data(self) :
        print("save_data fonksiyonu çalıştı")
        ## ======================================================
        ## save data to excel
        ## get the save path from window
        file_path = self.file_path.text().strip()
        if not file_path :
            QMessageBox.information(self, "Warning", "Please select path for save data")

        ## ======================================================
        ## create save file name
        #now = datetime.now().strftime("%Y-%m-%d")
        now = datetime.timestamp(datetime.now())
        file_name = f'{now}.xlsx'

        ## ======================================================
        ## get data from window table
        try :
            writer = pd.ExcelWriter(f'{file_path}/{file_name}')
            ## ======================================================
            info_headers = [self.result_table.horizontalHeaderItem(i).text() for i in range(self.result_table.columnCount())]
            info_df = pd.DataFrame(columns=info_headers)

            for row in range(self.result_table.rowCount()) :
                for col in range(self.result_table.columnCount()) :
                    info_df.at[row, info_headers[col]] = self.result_table.item(row, col).text()
            ## ======================================================
            ## save data to excel
            info_df.to_excel(writer, index= False)
            writer.save()

            ## ======================================================
            ## show message after save successfully
            QMessageBox.information(self, "Note","Save data successfully.") 
        except Exception as e :
            print("save data to excel fail")
            print(e)
            QMessageBox.information(self, "Note",f"Fail to save data to excel : {e}") 
        

  

      
        
def app() :
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())  
    

app()


