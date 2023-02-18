import mysql.connector


DBConnect = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "abc-python"
)

mycursor = DBConnect.cursor()
# mycursor.execute("CREATE TABLE customers (name VARCHAR (255), address VARCHAR(255))")
# mycursor.execute("DROP TABLE customers")



print(DBConnect)