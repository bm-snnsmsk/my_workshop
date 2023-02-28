from data_base import DataBase
import sqlite3
dataBase = DataBase('library.db')
from datetime import datetime
from datetime import timedelta





# conn = sqlite3.connect('library.db')
# curs = conn.cursor()


# sql1 = "SELECT * FROM books WHERE booksName = ?"


# sql2 = "SELECT * FROM books WHERE booksAuthorFirstName = ? AND booksAuthorLastName = ?"

# value1 = ["körlük"]
# value = ("jose","saramago",)

# conn.commit()
# #curs.execute(sql1,value1)
# # curs.execute(sql1,(value,))
# curs.execute(sql1,value1)

sql1 = "SELECT * FROM books"
sql2 = "SELECT * FROM books WHERE booksAuthorFirstName = ?"
sql3 = "SELECT * FROM books WHERE booksAuthorFirstName = ? AND booksAuthorLastName = ?"
sql4 = "UPDATE books SET booksState = 1 WHERE booksID = 2"
value = ["jose", "saramago"]
value1 = [int(1)]

# d = dataBase.getDatas(sql=sql1)['data']
# d = dataBase.getDatas(sql3, value)['data']
d = dataBase.updateData(sql4)['data']
# d = dataBase.updateData(sql4, [1, 2])['data']


# now = datetime.timestamp(datetime.now())
# after = datetime.timestamp(datetime.now() + timedelta(days = 15)) 
# print(now)
# print(after)

if d:
    print(f"uygun : {d}")
else :
    print(f"uygun : {d}")

# print(type(datetime.timestamp(datetime.now())))


