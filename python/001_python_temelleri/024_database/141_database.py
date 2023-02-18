import mysql.connector


DBConnect = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = ""
)

mycursor = DBConnect.cursor()
## mycursor.execute("CREATE DATABASE mydatabase")
# mycursor.execute("DROP DATABASE mydatabase")

# mycursor.execute("SHOW DATABASES")
# for i in mycursor :
#     print(i)



print(DBConnect)