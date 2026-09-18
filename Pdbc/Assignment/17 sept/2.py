# Database connectivity
import mysql.connector
conc = mysql.connector.connect(host="localhost",port=3306,user="root",password="root",database="assign")
print("Connection successful")
cursor = conc.cursor()
# Giving table definition and adding data
'''
cursor.execute("create table employee_pdbc(eid int primary key,ename varchar(50),department varchar(40),salary decimal(10,2),city varchar(30))")
data = [(201,"Amit","IT",45000.00,"Indore"),(202,"Priya","HR",40000.00,"Bhopal"),(203,"Rahul","IT",55000.00,"Indore"),(204,"Neha","Finance",50000.00,"Ujjain"),(205,"Karan","IT",60000.00,"Indore")]
query = "insert into employee_pdbc(eid,ename,department,salary,city) values(%s,%s,%s,%s,%s)"
cursor.executemany(query,data)
conc.commit()
'''
while True:
    print("""===== EMPLOYEE MANAGEMENT SYSTEM =====
        1. Add Employee
        2. Display All Employees
        3. Search Employee by Name
        4. Update Employee Salary
        5. Delete Employee
        6. Exit""")
    choice = int(input("Enter choice: "))
    
    match choice:
        case 1:
            id = int(input("Enter id"))
            name = (input("Enter name"))
            department = (input("Enter Department"))
            salary = float(input("Enter salary"))
            city = (input("Enter city"))
            query = "insert into employee_pdbc values(%s,%s,%s,%s,%s)"
            cursor.execute(query,(id,name,department,salary,city))
            conc.commit()
            print("Data inserted successfully")
            
        case 2:
            cursor.execute("select * from employee_pdbc")
            for rows in cursor.fetchall():
                print(rows)

        case 3:
            name = input("Enter employee name")
            query = "select * from employee_pdbc where ename like %s"
            cursor.execute(query,("%"+name+"%",))
            print("Matching Employees")
            for rows in  cursor.fetchall():
                print(rows)

        case 4:
            id = int(input("Enter id"))
            salary = float(input("Enter salary"))
            query = "update employee_pdbc set salary= %s where eid = %s"
            cursor.execute(query,(salary,id))
            conc.commit()
            print("Employee salary updated successfully.")

        case 5:
            id = int(input("Enter id"))
            query = "delete from employee_pdbc where eid=%s"
            cursor.execute(query,(id,))
            conc.commit()
            print("Employee deleted successfully.")

        case 6:
            print("Thank you for using Employee Management System.")
            break