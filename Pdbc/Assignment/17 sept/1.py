# Database connectivity
import mysql.connector
conc = mysql.connector.connect(host="localhost",port=3306,user="root",password="root",database="assign")
print("Connection successful")

while True:
    print("""===== STUDENT MANAGEMENT SYSTEM =====
    1. Add Student
    2. Display All Students
    3. Search Student by Name
    4. Update Student Fees
    5. Delete Student
    6. Exit""")
    choice = int(input("Enter choice: "))
    cursor = conc.cursor()
    match choice:
        case 1:
            sid = int(input("Enter Student id"))
            sname = (input("Enter Student name"))
            course = (input("Enter Student course"))
            fees = float(input("Enter Student fees"))
            city = (input("Enter Student city"))
            query = "insert into student_pdbc values(%s,%s,%s,%s,%s)"
            cursor.execute(query,(sid,sname,course,fees,city))
            conc.commit()
            print("Student Inserted Successfully")

        case 2:
            cursor.execute("Select * from student_pdbc")
            for rows in  cursor.fetchall():
                print(rows)

        case 3:
            name = input("Enter student name")
            query = "select * from student_pdbc where sname like %s"
            cursor.execute(query,("%"+name+"%",))
            print("Matching Students")
            for rows in  cursor.fetchall():
                    print(rows)

        case 4:
            id = int(input("Enter id "))
            fees = float(input("Enter fees"))
            query = "update student_pdbc set fees = %s where sid = %s"
            cursor.execute(query,(fees,id))
            print("Student fees updated successfully")


        case 5:
            id = int(input("Enter id "))
            query = "delete from student_pdbc where sid =%s"
            cursor.execute(query,(id,))
            conc.commit()
        case 6:
            print("Thank you for using Student Management System.")
            break


