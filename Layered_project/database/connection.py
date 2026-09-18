import mysql.connector
class Database:
    def connect(self):
        connection = mysql.connector.connect(host="localhost",user="root",password="root",database="batch18")
        return connection
        
