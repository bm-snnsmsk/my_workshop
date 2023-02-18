import mysql.connector as conn
import db


# DBConnect =conn.connect(
#     host = "localhost",
#     user = "root",
#     password = "",
#     database = "abc-python"
# )

# sql = "INSERT INTO urunler (urunName, urunPrice, urunDescription) VALUES(%s, %s, %s)"
# curs = DBConnect.cursor()
# values = ("iphone 7",3000,"4.5G uyumlu")
# curs.execute(sql, values)

# try :
#     DBConnect.commit()
# except conn.Error as e :
#     print(e)
# finally :
#     DBConnect.close()


##tek veri gönderme
## db.insertData("iphone 12",1100,"güzel telefon")


## çoklu veri gönderme
liste = [("nokia","2750", "kayıtlı"),
    ("casper","13700", "kayıtlı"),
    ("lenovo","13000", "kayıtsız")]
## liste.append(())
db.insertDatas(liste)
