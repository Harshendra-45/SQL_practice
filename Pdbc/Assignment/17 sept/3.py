# Database connectivity
import mysql.connector
conc = mysql.connector.connect(host="localhost",port=3306,user="root",password="root",database="assign")
print("Connection successful")
cursor = conc.cursor()

# Table definition and insertion 
'''
cursor.execute("create table product_pdbc(pid int primary key,pname varchar(60),category varchar(40),price decimal(10,2),quantity int)")
data = [(301,"Laptop","Electronics",55000.00,10),(302,"Mouse","Electronics",800.00,50),(303,"Keyboard","Electronics",1500.00,30),(304,"Notebook","Stationery",100.00,100),(305,"Pen","Stationery",20.00,200)]
query = "insert into product_pdbc values(%s,%s,%s,%s,%s)"
cursor.executemany(query,data)
print("Successful")
conc.commit()
'''

while True:
    print("""===== PRODUCT INVENTORY SYSTEM =====
    1. Add Product
    2. Display All Products
    3. Search Product by Name
    4. Update Product Price
    5. Delete Product
    6. Exit""")
    choice = int(input("Enter choice: "))
    
    match choice:
        case 1:
            id = int(input("Enter id"))
            name = (input("Enter name"))
            category = (input("Enter category"))
            price = float(input("Enter price"))
            quantity = int(input("Enter quantity"))
            query = "insert into product_pdbc values(%s,%s,%s,%s,%s)"
            cursor.execute(query,(id,name,category,price,quantity))
            conc.commit()
            print("Data inserted successfully")
            
        case 2:
            cursor.execute("select * from product_pdbc")
            for rows in cursor.fetchall():
                print(rows)

        case 3:
            name = input("Enter product name")
            query = "select * from product_pdbc where pname like %s"
            cursor.execute(query,("%"+name+"%",))
            print("Matching products")
            for rows in  cursor.fetchall():
                print(rows)

        case 4:
            id = int(input("Enter id"))
            price = float(input("Enter price"))
            query = "update product_pdbc set price= %s where pid = %s"
            cursor.execute(query,(price,id))
            conc.commit()
            print("Product price updated successfully.")

        case 5:
            id = int(input("Enter id"))
            query = "delete from product_pdbc where pid=%s"
            cursor.execute(query,(id,))
            conc.commit()
            print("Product deleted successfully.")

        case 6:
            print("Thank you for using Product Inventory System.")
            break

