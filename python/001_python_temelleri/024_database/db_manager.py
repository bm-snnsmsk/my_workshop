import mysql.connector as conn
from datetime import datetime



class db :
    def __init__(self) :
        self.DBConnect =conn.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "abc-python")
        self.curs = self.DBConnect.cursor() 

    def insertData(self,name, price, desc) :
        sql = "INSERT INTO urunler (urunName, urunPrice, urunDescription) VALUES(%s, %s, %s)"       
        values = (name,price,desc)
        self.curs.execute(sql, values)
        try :
            self.DBConnect.commit()
            print(f"{self.curs.rowcount} tane kayıt eklendi")
            print(f"son eklenen kaydın id : {self.curs.lastrowid}")
        except conn.Error as e :
            print(e)
   
    def insertDatas(self,liste) :
        sql = "INSERT INTO urunler (urunName, urunPrice, urunDescription) VALUES(%s, %s, %s)"
        curs = self.DBConnect.cursor()
        values = liste
        curs.executemany(sql, values)
        try :
            self.DBConnect.commit()
            print(f"{curs.rowcount} tane kayıt eklendi")
            print(f"son eklenen kaydın id : {curs.lastrowid}")
        except conn.Error as e :
            print(e)
        finally :
            self.DBConnect.close()
            print("database kapatıldı")
    
    def getData(self) :
        sql = "SELECT * FROM urunler"
        self.curs.execute(sql)
        try :       
            result = self.curs.fetchone()
            return result
        except conn.Error as e :
            print(e)

    def getDatas(self) :
            sql = "SELECT * FROM urunler"
            curs = self.DBConnect.cursor()
            curs.execute(sql)    
            try :       
                result = curs.fetchall()
                return result
            except conn.Error as e :
                print(e)
            finally :
                self.DBConnect.close()

    def getDatas2(self) :
        sql = "SELECT * FROM urunler WHERE id = %s AND name = %s"
        curs = self.DBConnect.cursor()
        pars = (2, 'Samsung S6')
        curs.execute(sql, params=pars)    
        try :       
            result = curs.fetchall()
            return result
        except conn.Error as e :
            print(e)
        finally :
            self.DBConnect.close()
    def updateData(self,name, id) :
            sql = "UPDATE urunler SET urunName = %s WHERE urunID = %s"            
            values = (name, id)
            self.curs.execute(sql, values)
            try :
                self.DBConnect.commit()
                print(f"{self.curs.rowcount} tane kayıt eklendi")
            except conn.Error as e :
                print(e)

    def deleteData(self,id) :
            sql = "DELETE FROM urunler WHERE urunID = %s"
            values = (id,)
            self.curs.execute(sql,values)
            try :
                self.DBConnect.commit()
                print(f"{self.curs.rowcount} tane kayıt eklendi")
            except conn.Error as e :
                print(e)
                
    def __del__(self) :  
           self.DBConnect.close()
           print("database kapatıldı")
