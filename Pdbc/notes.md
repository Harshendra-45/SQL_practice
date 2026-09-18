# PDBC
Python database connectivity is a mechanism that enables python applications to communicate with relational databases, using standarized API. Python follows a standard called `python DB-API 2.0`.  
* This ensures that different database modules behave similarly.  
* Before DB-API every database had its own way of connecting and executing queries.DB-API provides common standard code becomes quotable, consistent, easy to maintain.  
* It is not a library, it's a set of rules.

## Advantages of DB_API
1. Database Independent.
2. easy to switch,
3. standard coding style.
4. secure(it supports parameterized queries)
5. Reduce development time.

## Python database modules(driver)
To connect python with database we use specific libraries, 
* For MySql : mysql-connector-python,PyMySQL
* PostgreSQl psycopg2
* SQLite sqlite3 (built-in)
* Oracle cx_Oracle
* MongoDB pymongo

A database driver or module is a python library that allows your program to connect to a database,execute sql queries and fetch results.  
These modules follow PEP249-- that's why their structure is similar (pep-python enhancement proposal,249- proposal number).  
These proposal tells how python database modules should behave and what methods they must provide.

## Database connectivity architecture
```
User/application program 
       |
    DB-API 2.0 interface(PEP 249)
            |
        Database driver(mysql-connector)
                |
            Database Server(mysql/postgresql)
                    |
                Data Storage
```
## Steps for connecting python with database 
1. Import database module (after installation is done )
2. Establish connection 
3. Create cursor object
4. Execute Sql Queries 
5. Fetch results 
6. Commit transaction, if needed
7. Close connection 
```
import mysql.connector
try:
    con = mysql.connector.connect(host="localhost",port=3306,user="root",password="root",database="batch18")
    if con.is_connected():
        print("connection established")
except Exception as e:
    print("Something went wrong",e)
finally:
    print("Finally runnuing")
    con.close()
    print("connection closed")
```

**Create cursor object**:
In python db connectivity a cursor object is used to interact with the database,it acts like a bridge between your python code and the database, a cursor is an object that allows you to execute sql queries, fetch results from database etc. 
* Even after establishing a connection we cannot execute sql queries directly using the connection object, we must create a cursor object bcoz it provide methods like `execute()`,`fetchone()`,`fetchall()`, it manages query execution, it handles result sets.
```
syntax for connecting cursor
cursor=connection.cursor()
```
* cursor.execute(): it is a method used to send sql commands to the database through a cursor object, means it tells the database that run this sql query 
```
cursor.execute(query,values)
query--sql statements(insert,delete,update etc.)
values--optional . tuple of values to insert in db
```
```
import mysql.connector
try:
    con = mysql.connector.connect(host="localhost",port=3306,user="root",password="root",database="batch18")
    if con.is_connected():
        print("connection established")
    cursor=con.cursor()
    query="create table pdemployee1(id int primary key, name varchar(20),salary decimal(10,2))"
    cursor.execute(query)
    
except Exception as e:
    print("Something went wrong",e)
finally:
    print("Finally runnuing")
    con.close()
    print("connection closed")
```

**Insert data** 

```
import mysql.connector
try:
    con = mysql.connector.connect(host="localhost",port=3306,user="root",password="root",database="batch18")
    if con.is_connected():
        print("connection established")
    cursor=con.cursor()
    query="insert into pdemployee1 values(1,'dipu',20101)"
    cursor.execute(query)
    print("data inserted")
    con.commit()
except Exception as e:
    print("Something went wrong",e)
finally:
    print("Finally runnuing")
    con.close()
    print("connection closed")
```
```
mysql> use batch18;
Database changed
mysql> desc pdemployee1;
+--------+---------------+------+-----+---------+-------+
| Field  | Type          | Null | Key | Default | Extra |
+--------+---------------+------+-----+---------+-------+
| id     | int           | NO   | PRI | NULL    |       |
| name   | varchar(20)   | YES  |     | NULL    |       |
| salary | decimal(10,2) | YES  |     | NULL    |       |
+--------+---------------+------+-----+---------+-------+
3 rows in set (0.05 sec)

mysql> select * from pdemployee1;
Empty set (0.00 sec)

mysql> select * from pdemployee1;
+----+------+----------+
| id | name | salary   |
+----+------+----------+
|  1 | dipu | 20101.00 |
+----+------+----------+
1 row in set (0.00 sec)

mysql> select * from pdemployee1;
+----+------+----------+
| id | name | salary   |
+----+------+----------+
|  1 | dipu | 20101.00 |
|  2 | Ram  | 30101.00 |
+----+------+----------+
2 rows in set (0.00 sec)
```

**execute many**: It is a method of the cursor object used to execute the same sql query multiple times with different values.  
* Instead of inserting one record again and again using execute, we can insert multiple records at a time. 
```
cursor.executemany(query,datalist)
query : sql statement with placeholder(%s)
datalist: list of tuples
```
```
....
    cursor=con.cursor()
    query="insert into pdemployee1(id,name,salary) values(%s,%s,%s)"
    data=[(101,"deepika",5000),(102,"rashmika",70000),(103,"virat",80000)]
    cursor.executemany(query,data)
    print("data inserted")
    con.commit()
....
```

Read data from user
```
cursor=con.cursor()
    query="insert into pdemployee1(id,name,salary) values(%s,%s,%s)"
    n = int(input("Enter no of details"))
    data=[]
    for i in range(n+1):
        print("Enter details")
        id=int(input("Enter employee id"))
        name=(input("Enter employee name"))
        salary=float(input("Enter salary"))
        data.append((id,name,salary))    
    cursor.executemany(query,data)
    print("data inserted")
    con.commit()
```

## Fetching data
Fetching data means retreiving rows from the database table,after executing select query.
```
cursor.execute("select * from tablename")

```
This statement loads the result into the cursor object, there are different fetching methods provided by python to fetch data from the result set.

1. Fetchone():This function fetch one row at a time
```
row=cursor.fetchone()
```
* It returns a single tuple and after that cursor move to the next row after each call.
* It returns none when no more data is available

2. fetchmany(size): It fetches specified no of rows 

3. fetchall(): It fetches all the rows at once
* It returns a list of tuples

```
    cursor=con.cursor()
    cursor.execute("select * from pdemployee1")
    print("using fetch one")
    print(cursor.fetchone())
    print("using fetch many")
    print(cursor.fetchmany(2))
    print("using fetch all")
    print(cursor.fetchall())
```
```
cursor=con.cursor()
cursor.execute("select * from pdemployee1")
for row in cursor :
    print(row)
```

**Accessing column value**:  
By default rows are tuple we can access values by index.
```
cursor=con.cursor()
cursor.execute("select * from pdemployee1")
row = cursor.fetchone()
print(row[0])
print(row[1])
print(row[2])
```

## Using dictionary cursor
If we want data in key-value pair then we can use dictionary cursor.
```
cursor=con.cursor(dictionary=True)
cursor.execute("select * from pdemployee1")
row = cursor.fetchone()
print(row)
print(row['name'])
```
## Queries 
WAQ in pdbc to fetch employees whose salary>60000?
```
cursor=con.cursor()
cursor.execute("select * from pdemployee1 where salary>60000")
for row in cursor:
    print(row)
```

WAQ to fetch and count records available in table
```
cursor=con.cursor()
cursor.execute("select * from pdemployee")
rows=cursor.fetchall()
print(len(rows))
```

WAQ to display employee details whose name is taken from user
```
name = input("enter name")
cursor=con.cursor()
cursor.execute("select * from pdemployee1 where name='"+name+"'")
rows=cursor.fetchall()
print(rows)
```
```
cursor=con.cursor()
query = "select * from pdemployee1 where name=%s"
cursor.execute(query,(name,))
rows=cursor.fetchall()
print(rows)
```

## SQL Injection :
Sql injection is a security vulnerability  where a user can manipulate the SQL Query by entering malicious input.
```
select * from tablename where username=" " or "1"="1";
```
The above condition will always be true and it will return all rows of table.

## Dynamic Query with where clause
1. WAQ to read name and salary from user and fetch that record
```
name = input("enter name")
salary=float(input("Enter salary"))
cursor=con.cursor()
query = "select * from pdemployee1 where name=%s and salary>%s"
cursor.execute(query,(name,salary))
rows=cursor.fetchall()
print(rows)

Out:
connection established
enter namevirat
Enter salary5000
[(103, 'virat', Decimal('80000.00'))]
```

## Dynamic insert
```
id = int(input("Enter id"))
name = input("enter name")
salary=float(input("Enter salary"))
cursor=con.cursor()
query = "insert into pdemployee1 values(%s,%s,%s)"
cursor.execute(query,(id,name,salary))
con.commit()
```
1. WAQ to update salary of an employee based on id
```
id = int(input("Enter id"))
salary=float(input("Enter salary"))
cursor=con.cursor()
query = "update pdemployee1 set salary=%s where id= %s"
cursor.execute(query,(salary,id))
con.commit()
```

2. WAQ to delete any employee based on id
```
id = int(input("Enter id"))
cursor=con.cursor()
query = "delete from pdemployee1 where id =%s"
cursor.execute(query,(id,))
con.commit()
```

## Dynamic Query with like
1. Show all employees whose name ends with a
```
name = input("Enter name")
cursor=con.cursor()
query = "select * from pdemployee1 where name like %s"
cursor.execute(query,("%"+name,))  `this is main`
for row in cursor.fetchall():
        print(row)
con.close()   
```
If we change "%" position we can do start with end with to match patterns

**Dynamic Query with in operator** 
```
cursor=con.cursor()
ids = [102,103,106]
query = "select * from pdemployee1 where id in (%s,%s,%s)"
cursor.execute(query,tuple(ids))
for row in cursor.fetchall():
        print(row)
con.close()    

(102, 'rashmika', Decimal('70000.00'))
(103, 'virat', Decimal('80000.00'))
(106, 'harsh', Decimal('8054555.00'))
```

## H.W
1. Perform group by, having , order by , limit , offset , foreign key , joins , subqueries

# Layered Architecture
It is a software design approach in which an application is divided into multiple layers and each layer has a specific responsibility.





