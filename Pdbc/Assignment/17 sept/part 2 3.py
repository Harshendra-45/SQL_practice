import mysql.connector
conc = mysql.connector.connect(host="localhost",port=3306,user="root",password="root",database="assign")
print("Connection successful")
cursor = conc.cursor()

# Display all products from Electronics category.
query = '''select * from product_pdbc where category="Electronics"'''
cursor.execute(query)
for i in cursor.fetchall():
    print(i)

# Display all products from Stationery category.
query = '''select * from product_pdbc where category="stationary"'''
cursor.execute(query)
for i in cursor.fetchall():
    print(i)

#  Search products whose names contain 'oo'.
name = input("Enter product name")
query = "select * from product_pdbc where pname like %s"
cursor.execute(query,("%"+name+"%",))
print("Matching products")
for rows in  cursor.fetchall():
    print(rows)

# Search products whose names start with 'M'.
name = input("Enter product name")
query = "select * from product_pdbc where pname like %s"
cursor.execute(query,("%"+name,))
print("Matching products")
for rows in  cursor.fetchall():
    print(rows)

# Search products whose names end with 'e'.
name = input("Enter product name")
query = "select * from product_pdbc where pname like %s"
cursor.execute(query,(name+"%",))
print("Matching products")
for rows in  cursor.fetchall():
    print(rows)

# Display products whose price is greater than 1000.
query = '''select * from product_pdbc where price>1000'''
cursor.execute(query)
for i in cursor.fetchall():
    print(i)

# 7. Display products whose quantity is less than 20.
query = '''select * from product_pdbc where quantity<20'''
cursor.execute(query)
for i in cursor.fetchall():
    print(i)

# Update product quantity.
query = '''update product_pdbc set quantity = 20 where pid = 302'''
cursor.execute(query)
conc.commit()

# Update product category.
query = '''update product_pdbc set category = "Electric" where pid = 302'''
cursor.execute(query)
conc.commit()

# Delete a product by ID.
query = '''delete from product_pdbc where pid = 302'''
cursor.execute(query)
conc.commit()

# Display products whose category contains 'tron'.
query = 'select * from product_pdbc where category like "%tron"'
cursor.execute(query)
print("Matching products")
for rows in  cursor.fetchall():
    print(rows)

# Search products by a user-provided price range.
price = int(input("Enter price"))
query = 'select * from product_pdbc where price<%s'
cursor.execute(query,(price,))
print("Matching products")
for rows in  cursor.fetchall():
    print(rows)