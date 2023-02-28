import sqlite3


class DataBase() :
    def __init__(self,database_name) :
        self.DBConnect = sqlite3.connect(database_name)
        self.curs = self.DBConnect.cursor()
        self.DBConnect.commit()
    
    ### tekrarlayan kodlar fonksiyonu START
    def common_codes(self, sql, values) :
        if values == False :
            return self.curs.execute(sql)
        else :
            return self.curs.execute(sql, values) ### values değerleri istenecek olan yerde  => values = [] şeklinde istenmeli
    ### tekrarlayan kodlar fonksiyonu END

    def create_table(self, sql, values = False) :
        self.common_codes(sql, values)
        try :
            data = self.DBConnect.commit()
            return { "message" : "Tablo başarılı bir şekilde oluşturuldu", "data" : data}
        except Exception as e :
            return { "message" : "Tablo oluşturulma sırasında beklenmeyen bir hata meydana geldi : "+ str(e)}
    
    def  insertData(self,sql, values = False) :
        self.common_codes(sql, values)
        try :            
            self.DBConnect.commit()
            return { "message" : "Veriler başarılı bir şekilde tabloya eklendi", "data" : self.curs.rowcount}
        except Exception as e :
            return { "message" : "Kayıt eklenme sırasında beklenmeyen bir hata meydana geldi : "+ str(e)}
    
    def getData(self,sql, values = False) : 
        self.common_codes(sql, values)
        try :
            data = self.curs.fetchone()
            return { "message" : "Veriler başarılı bir şekilde tablodan çekildi", "data" : data}
        except Exception as e :
            return { "message" : "Kayıt çekme sırasında beklenmeyen bir hata meydana geldi : "+ str(e)}

    def getDatas(self,sql, values = False) : 
        self.common_codes(sql, values)
        try : 
            data = self.curs.fetchall()
            return { "message" : "Veriler başarılı bir şekilde tablodan çekildi", "data" : data}
        except Exception as e :
            return { "message" : "Kayıt çekme sırasında beklenmeyen bir hata meydana geldi : "+ str(e)}

    def updateData(self, sql, values = False) :
        self.common_codes(sql, values)
        try : 
            self.DBConnect.commit()
            return { "message" : "Kayıt başarılı bir şekilde güncellendi", "data" : self.curs.rowcount}
        except Exception as e :
            return { "message" : "Kayıt güncelleme sırasında beklenmeyen bir hata meydana geldi : "+ str(e)}

    def deleteData(self, sql, values = False) :  
        self.common_codes(sql, values)
        try :
            self.DBConnect.commit()
            return { "message" : "Kayıt başarılı bir şekilde silindi", "data" : self.curs.rowcount}
        except Exception as e :
            return { "message" : "Kayıt silinme sırasında beklenmeyen bir hata meydana geldi : "+ str(e)}

    def __del__(self) :
        self.DBConnect.close()


