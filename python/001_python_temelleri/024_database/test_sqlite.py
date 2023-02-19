import sqlite3

connectDB = sqlite3.connect("chinook.db")
curs = connectDB.cursor()
curs.execute("SELECT * FROM customers WHERE FirstName LIKE 'a%' ")
result = curs.fetchall()
#print(result)
for i in result :
    print(i[1])
connectDB.close()
