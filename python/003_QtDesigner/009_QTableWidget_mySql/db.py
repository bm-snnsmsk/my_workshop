import mysql.connector as conn

DBConnect =conn.connect(
host = "localhost",
user = "root",
password = "",
database = "abc-kurs")


# def insertData(name, price, desc) :
#     sql = "INSERT INTO urunler (urunName, urunPrice, urunDescription) VALUES(%s, %s, %s)"
#     curs = DBConnect.cursor()
#     values = (name,price,desc)
#     curs.execute(sql, values)
#     try :
#         DBConnect.commit()
#         print(f"{curs.rowcount} tane kayıt eklendi")
#         print(f"son eklenen kaydın id : {curs.lastrowid}")
#     except conn.Error as e :
#         print(e)
#     finally :
#         DBConnect.close()
#         print("database kapatıldı")

# def insertDatas(liste) :
#     sql = "INSERT INTO urunler (urunName, urunPrice, urunDescription) VALUES(%s, %s, %s)"
#     curs = DBConnect.cursor()
#     values = liste
#     curs.executemany(sql, values)
#     try :
#         DBConnect.commit()
#         print(f"{curs.rowcount} tane kayıt eklendi")
#         print(f"son eklenen kaydın id : {curs.lastrowid}")
#     except conn.Error as e :
#         print(e)
#     finally :
#         DBConnect.close()
#         print("database kapatıldı")

# def getData() :
#     sql = "SELECT * FROM urunler"
#     curs = DBConnect.cursor()
#     curs.execute(sql)
#     try :       
#         result = curs.fetchone()
#         return result
#     except conn.Error as e :
#         print(e)
#     finally :
#         DBConnect.close()

def getDatas() :
    sql = "SELECT * FROM siparis"
    curs = DBConnect.cursor()
    curs.execute(sql)    
    try :       
        result = curs.fetchall()
        return result
    except conn.Error as e :
        print(e)
    finally :
        DBConnect.close()

# def getDatas2() :
#     sql = "SELECT * FROM urunler WHERE id = %s AND name = %s"
#     curs = DBConnect.cursor()
#     pars = (2, 'Samsung S6')
#     curs.execute(sql, params=pars)    
#     try :       
#         result = curs.fetchall()
#         return result
#     except conn.Error as e :
#         print(e)
#     finally :
#         DBConnect.close()

# def updateData(name, id) :
#     sql = "UPDATE urunler SET urunName = %s WHERE urunID = %s"
#     curs = DBConnect.cursor()
#     values = (name, id)
#     curs.execute(sql, values)
#     try :
#         DBConnect.commit()
#         print(f"{curs.rowcount} tane kayıt eklendi")
#     except conn.Error as e :
#         print(e)
#     finally :
#         DBConnect.close()
#         print("database kapatıldı")

# def deleteData(id) :
#     sql = "DELETE FROM urunler WHERE urunID = %s"
#     curs = DBConnect.cursor()
#     values = (id,)
#     curs.execute(sql,values)
#     try :
#         DBConnect.commit()
#         print(f"{curs.rowcount} tane kayıt eklendi")
#     except conn.Error as e :
#         print(e)
#     finally :
#         DBConnect.close()
#         print("database kapatıldı")

# def deneme() :
#     print("deneme------------------")

