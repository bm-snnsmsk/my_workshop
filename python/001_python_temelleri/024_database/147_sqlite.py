import sqlite3

## server tabanlı sql'den tek farkı bağlantı ile ilgili kod
conn = sqlite3.connect("deneme.db") ## db dosyası bu dizinde yoksa oluşturur

## bundan sonrası mysql ile aynı
curs = conn.cursor()
curs.execute("select * from customers")
result = curs.fetchall()
print(result)
conn.close()