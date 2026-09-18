from database.connection import Database

class EmployeeDao:
    def getemployee(self):
        print("dao getting employee data")
        db = Database()
        db.connect()

    def save_employee(self,employee):
        print("dao saving employee data")
        print("ID",employee.id)
        print("name",employee.name)
        print("salary",employee.salary)
        db = Database()
        conn = db.connect()
        cursor = conn.cursor()
        query="insert into pdemployee1(id,name,salary) values(%s,%s,%s)"
        data=(employee.id,employee.name,employee.salary)
        cursor.execute(query,data)
        conn.commit()
        conn.close()
        
