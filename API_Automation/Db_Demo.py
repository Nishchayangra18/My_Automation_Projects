import mysql.connector
from Utilities.Configurations import *
#host, database, user, password
# # conn = mysql.connector.connect(host='localhost', database='APIDevelop', user='root', password='Nishchay@18')
# print(conn.is_connected())
conn = get_Database_Connection()
cursor = conn.cursor()
cursor.execute('select * from CustomerInfo')
# row = cursor.fetchone()
# print(row)
# print(row[3])
# rowAll = cursor.fetchall()  #List of Tupple
# print(rowAll)

rows = cursor.fetchall()
print(type(rows))
print(rows)
sum = 0
for row in rows:
    print(row[2])
    sum += row[2]
print(sum)

query = "update customerinfo set Location = %s where CourseName = %s"
data = ("UK","selenium")
cursor.execute(query,data)
conn.commit()

conn.close()