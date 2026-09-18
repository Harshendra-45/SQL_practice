import mysql.connector
con = mysql.connector.connect(host="localhost",port=3306,user="root",password="root",database="batch18")
if con.is_connected():
        print("connection established")
cursor=con.cursor()
ids = (102,103,106)
query = "select * from pdemployee1 where id in %s"
cursor.execute(query,ids)
for row in cursor.fetchall():
        print(row)
con.close()    
