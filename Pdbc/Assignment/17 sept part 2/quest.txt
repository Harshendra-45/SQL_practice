ASSIGNMENT 1: ONLINE SHOPPING ORDER MANAGEMENT SYSTEM
======================================================

An online shopping company wants to manage customers, products, and orders
using Python Database Connectivity (PDBC).

Students must use Python mysql.connector and MySQL.


DATABASE TABLES
===============

TABLE 1: customer_order_pdbc
----------------------------
Column       Data Type
--------------------------------
customer_id  INT PRIMARY KEY
customer_name VARCHAR(60)
city         VARCHAR(40)
email        VARCHAR(80)

SAMPLE DATA
-----------
customer_id  customer_name  city       email
---------------------------------------------------------
1            Amit           Indore     amit@gmail.com
2            Priya          Bhopal     priya@gmail.com
3            Rahul          Indore     rahul@gmail.com
4            Neha           Ujjain     neha@gmail.com
5            Karan          Dewas      karan@gmail.com


TABLE 2: product_order_pdbc
---------------------------
Column       Data Type
--------------------------------
product_id   INT PRIMARY KEY
product_name VARCHAR(80)
category     VARCHAR(40)
price        DECIMAL(10,2)
stock        INT

product_id  product_name  category       price      stock
------------------------------------------------------------
101         Laptop        Electronics    55000.00   10
102         Mouse         Electronics      800.00   50
103         Keyboard      Electronics     1500.00   30
104         Notebook      Stationery       100.00  100
105         Monitor       Electronics    12000.00   15
106         Pen            Stationery        20.00  200


TABLE 3: customer_order_details
-------------------------------
Column       Data Type
--------------------------------
order_id     INT PRIMARY KEY
customer_id  INT
product_id   INT
quantity     INT
order_status VARCHAR(30)

Foreign keys:
customer_id references customer_order_pdbc(customer_id)
product_id references product_order_pdbc(product_id)

SAMPLE DATA
-----------
order_id  customer_id  product_id  quantity  order_status
------------------------------------------------------------
1001      1            101          1         Delivered
1002      1            102          2         Delivered
1003      2            103          1         Shipped
1004      3            105          2         Delivered
1005      3            104          5         Pending
1006      4            101          1         Pending
1007      5            106          10        Delivered


MENU
====

===== ONLINE SHOPPING ORDER MANAGEMENT =====
1. Add Customer
2. Add Product
3. Place Order
4. Display All Orders with Customer and Product Details
5. Search Customer by Name
6. Update Product Price
7. Update Order Status
8. Delete Order
9. Display Customer-wise Total Purchase Amount
10. Display Products Costing More Than Average Product Price
11. Display Customers Who Have Placed at Least One Order
12. Display Customers Who Have Not Placed Any Order
13. Exit

Enter your choice:


TASKS AND EXPECTED INPUT/OUTPUT
==============================

1. ADD CUSTOMER
---------------

INPUT
-----
Enter your choice: 1
Enter Customer ID: 6
Enter Customer Name: Anjali
Enter City: Indore
Enter Email: anjali@gmail.com

OUTPUT
------
Customer inserted successfully.


2. ADD PRODUCT
-------------

INPUT
-----
Enter your choice: 2
Enter Product ID: 107
Enter Product Name: Headphones
Enter Category: Electronics
Enter Price: 2500
Enter Stock: 25

OUTPUT
------
Product inserted successfully.


3. PLACE ORDER
--------------

INPUT
-----
Enter your choice: 3
Enter Order ID: 1008
Enter Customer ID: 6
Enter Product ID: 107
Enter Quantity: 2
Enter Order Status: Pending

OUTPUT
------
Order placed successfully.


4. DISPLAY ALL ORDERS USING INNER JOIN
--------------------------------------

REQUIRED OPERATION
------------------
Display order ID, customer name, product name, quantity, price,
calculated amount, and order status.

Calculated amount = quantity * price

EXPECTED OUTPUT
---------------
Order ID  Customer Name  Product Name  Quantity  Price     Amount    Status
----------------------------------------------------------------------------
1001      Amit           Laptop         1        55000.00  55000.00  Delivered
1002      Amit           Mouse          2          800.00   1600.00  Delivered
1003      Priya          Keyboard       1         1500.00   1500.00  Shipped
1004      Rahul          Monitor        2        12000.00  24000.00  Delivered
1005      Rahul          Notebook       5          100.00    500.00  Pending
1006      Neha           Laptop         1        55000.00  55000.00  Pending
1007      Karan          Pen            10          20.00    200.00  Delivered


5. SEARCH CUSTOMER USING LIKE
-----------------------------

INPUT
-----
Enter your choice: 5
Enter customer name to search: an

OUTPUT
------
Customer ID  Customer Name  City
-------------------------------------
1            Amit           Indore
5            Karan          Dewas

Note:
Use LIKE '%an%' in the SQL query.
The result may include names containing the entered text.


6. UPDATE PRODUCT PRICE
-----------------------

INPUT
-----
Enter your choice: 6
Enter Product ID: 102
Enter New Price: 900

OUTPUT
------
Product price updated successfully.


7. UPDATE ORDER STATUS
----------------------

INPUT
-----
Enter your choice: 7
Enter Order ID: 1005
Enter New Status: Delivered

OUTPUT
------
Order status updated successfully.


8. DELETE ORDER
---------------

INPUT
-----
Enter your choice: 8
Enter Order ID: 1007

OUTPUT
------
Order deleted successfully.


9. CUSTOMER-WISE TOTAL PURCHASE AMOUNT
--------------------------------------

REQUIRED SQL CONCEPTS
---------------------
INNER JOIN
GROUP BY
SUM()
ORDER BY

Required output columns:
Customer ID, Customer Name, Total Purchase Amount

EXPECTED OUTPUT
---------------
Customer ID  Customer Name  Total Purchase Amount
--------------------------------------------------
1            Amit           56600.00
2            Priya           1500.00
3            Rahul          24500.00
4            Neha           55000.00
5            Karan           200.00

Formula:
SUM(order_quantity * product_price)


10. PRODUCTS COSTING MORE THAN AVERAGE PRICE
--------------------------------------------

REQUIRED CONCEPT
----------------
Single-row subquery.

Question:
Display products whose price is greater than the average price
of all products.

EXPECTED OUTPUT
---------------
Product ID  Product Name  Price
-------------------------------------
101         Laptop         55000.00
105         Monitor        12000.00


11. CUSTOMERS WHO HAVE PLACED AT LEAST ONE ORDER
------------------------------------------------

REQUIRED CONCEPT
----------------
Subquery using IN or EXISTS.

Question:
Display customers who have placed at least one order.

EXPECTED OUTPUT
---------------
Customer ID  Customer Name
--------------------------
1            Amit
2            Priya
3            Rahul
4            Neha
5            Karan


12. CUSTOMERS WHO HAVE NOT PLACED ANY ORDER
-------------------------------------------

REQUIRED CONCEPT
----------------
LEFT JOIN with IS NULL
OR NOT EXISTS subquery.

Question:
Display customers who have never placed an order.

EXPECTED OUTPUT
---------------
Customer ID  Customer Name
--------------------------
6            Anjali

Note:
This output assumes customer 6 was inserted but has not placed an order.


13. FOREIGN KEY TEST
--------------------

Try to place an order with a customer ID that does not exist.

INPUT
-----
Enter your choice: 3
Enter Order ID: 1009
Enter Customer ID: 999
Enter Product ID: 101
Enter Quantity: 1
Enter Order Status: Pending

EXPECTED OUTPUT
---------------
Order could not be inserted because the customer ID
does not exist in the parent table.

Students should observe the foreign key constraint error.


14. MENU VALIDATION
-------------------

If the user enters an invalid menu choice:

INPUT
-----
Enter your choice: 20

OUTPUT
------
Invalid choice. Please try again.


============================================================
ASSIGNMENT 5: COMPANY DEPARTMENT AND EMPLOYEE ANALYSIS SYSTEM
============================================================

A company wants to manage departments and employees.
The system should support employee CRUD operations and analytical
queries using joins, foreign keys, and subqueries.

CONCEPTS TO PRACTICE
--------------------
1. Primary key
2. Foreign key
3. INSERT, SELECT, UPDATE, DELETE
4. INNER JOIN
5. LEFT JOIN
6. SELF JOIN
7. GROUP BY
8. HAVING
9. Aggregate functions
10. Single-row subquery
11. Multi-row subquery
12. Correlated subquery
13. LIKE operator
14. Menu-driven PDBC program


DATABASE TABLES
===============

TABLE 1: department_pdbc
------------------------
Column       Data Type
--------------------------------
dept_id      INT PRIMARY KEY
dept_name    VARCHAR(50)
location     VARCHAR(40)

SAMPLE DATA
-----------
dept_id  dept_name    location
------------------------------------
1        IT           Indore
2        HR           Bhopal
3        Finance      Indore
4        Sales        Ujjain
5        Training     Dewas


TABLE 2: employee_pdbc
----------------------
Column       Data Type
--------------------------------
emp_id      INT PRIMARY KEY
emp_name    VARCHAR(60)
salary      DECIMAL(10,2)
job_title   VARCHAR(50)
dept_id     INT
manager_id  INT NULL

Foreign keys:
dept_id references department_pdbc(dept_id)
manager_id references employee_pdbc(emp_id)

SAMPLE DATA
-----------
emp_id  emp_name  salary    job_title          dept_id  manager_id
-------------------------------------------------------------------
101     Amit      70000.00  Developer           1        NULL
102     Priya     55000.00  Tester              1        101
103     Rahul     90000.00  Manager             1        NULL
104     Neha      45000.00  HR Executive        2        NULL
105     Karan     80000.00  Finance Manager     3        NULL
106     Anjali    50000.00  Accountant          3        105
107     Vijay     40000.00  Sales Executive     4        NULL
108     Pooja     60000.00  Trainer             5        NULL


MENU
====

===== COMPANY EMPLOYEE MANAGEMENT SYSTEM =====
1. Add Department
2. Add Employee
3. Display All Employees with Department
4. Search Employee by Name
5. Update Employee Salary
6. Update Employee Department
7. Delete Employee
8. Display Department-wise Employee Count
9. Display Department-wise Average Salary
10. Display Employees Earning More Than Average Salary
11. Display Employees Earning More Than Their Department Average
12. Display Employees Working in the IT Department
13. Display Departments Having More Than One Employee
14. Display Employee and Manager Names using Self Join
15. Display Departments with No Employees
16. Test Foreign Key Constraint
17. Exit

Enter your choice:


TASKS AND EXPECTED INPUT/OUTPUT
==============================

1. ADD DEPARTMENT
-----------------

INPUT
-----
Enter your choice: 1
Enter Department ID: 6
Enter Department Name: Research
Enter Location: Indore

OUTPUT
------
Department inserted successfully.


2. ADD EMPLOYEE
---------------

INPUT
-----
Enter your choice: 2
Enter Employee ID: 109
Enter Employee Name: Rohan
Enter Salary: 48000
Enter Job Title: Developer
Enter Department ID: 6
Enter Manager ID: 101

OUTPUT
------
Employee inserted successfully.


3. DISPLAY EMPLOYEES WITH DEPARTMENT USING INNER JOIN
------------------------------------------------------

REQUIRED OUTPUT COLUMNS
-----------------------
Employee ID
Employee Name
Job Title
Salary
Department Name
Location

EXPECTED OUTPUT
---------------
Emp ID  Employee Name  Job Title          Salary     Department
-------------------------------------------------------------------
101     Amit           Developer           70000.00   IT
102     Priya          Tester              55000.00   IT
103     Rahul          Manager             90000.00   IT
104     Neha           HR Executive        45000.00   HR
105     Karan          Finance Manager     80000.00   Finance
106     Anjali         Accountant          50000.00   Finance
107     Vijay          Sales Executive     40000.00   Sales
108     Pooja          Trainer             60000.00   Training


4. SEARCH EMPLOYEE BY NAME USING LIKE
-------------------------------------

INPUT
-----
Enter your choice: 4
Enter employee name to search: an

OUTPUT
------
Emp ID  Employee Name  Job Title       Salary
------------------------------------------------
101     Amit           Developer        70000.00
106     Anjali         Accountant       50000.00

Use:
WHERE emp_name LIKE '%an%'


5. UPDATE EMPLOYEE SALARY
-------------------------

INPUT
-----
Enter your choice: 5
Enter Employee ID: 102
Enter New Salary: 60000

OUTPUT
------
Employee salary updated successfully.


6. UPDATE EMPLOYEE DEPARTMENT
-----------------------------

INPUT
-----
Enter your choice: 6
Enter Employee ID: 107
Enter New Department ID: 5

OUTPUT
------
Employee department updated successfully.


7. DELETE EMPLOYEE
------------------

INPUT
-----
Enter your choice: 7
Enter Employee ID: 108

OUTPUT
------
Employee deleted successfully.


8. DEPARTMENT-WISE EMPLOYEE COUNT
---------------------------------

REQUIRED CONCEPTS
-----------------
INNER JOIN
GROUP BY
COUNT()

EXPECTED OUTPUT
---------------
Department  Employee Count
--------------------------
IT           3
HR           1
Finance      2
Sales        1
Training     1


9. DEPARTMENT-WISE AVERAGE SALARY
---------------------------------

REQUIRED CONCEPTS
-----------------
INNER JOIN
GROUP BY
AVG()

EXPECTED OUTPUT
---------------
Department  Average Salary
--------------------------
IT           71666.67
HR           45000.00
Finance      65000.00
Sales        40000.00
Training     60000.00


10. EMPLOYEES EARNING MORE THAN OVERALL AVERAGE SALARY
------------------------------------------------------

REQUIRED CONCEPT
----------------
Single-row subquery.

Question:
Display employees whose salary is greater than the average salary
of all employees.

EXPECTED OUTPUT
---------------
Emp ID  Employee Name  Salary
-----------------------------
101     Amit           70000.00
103     Rahul          90000.00
105     Karan          80000.00
108     Pooja          60000.00

Note:
The exact output changes if students update or delete records.


11. EMPLOYEES EARNING MORE THAN THEIR DEPARTMENT AVERAGE
--------------------------------------------------------

REQUIRED CONCEPT
----------------
Correlated subquery.

Question:
Display employees whose salary is greater than the average salary
of their own department.

EXPECTED OUTPUT
---------------
Emp ID  Employee Name  Department  Salary
------------------------------------------
103     Rahul          IT          90000.00
105     Karan          Finance     80000.00


12. EMPLOYEES WORKING IN IT DEPARTMENT
--------------------------------------

REQUIRED CONCEPT
----------------
Subquery returning one value.

Question:
Display all employees who work in the IT department.

EXPECTED OUTPUT
---------------
Emp ID  Employee Name  Salary
-----------------------------
101     Amit           70000.00
102     Priya          55000.00
103     Rahul          90000.00


13. DEPARTMENTS HAVING MORE THAN ONE EMPLOYEE
---------------------------------------------

REQUIRED CONCEPTS
-----------------
JOIN
GROUP BY
HAVING

EXPECTED OUTPUT
---------------
Department  Employee Count
--------------------------
IT           3
Finance      2


14. EMPLOYEE AND MANAGER NAMES USING SELF JOIN
----------------------------------------------

REQUIRED CONCEPT
----------------
Self join.

Question:
Display employee name and manager name.

EXPECTED OUTPUT
---------------
Employee Name  Manager Name
--------------------------
Priya          Amit
Anjali         Karan


15. DEPARTMENTS WITH NO EMPLOYEES
---------------------------------

REQUIRED CONCEPT
----------------
LEFT JOIN with IS NULL.

Question:
Display departments that do not have any employees.

EXPECTED OUTPUT
---------------
Department ID  Department Name
-----------------------------
6              Research

Note:
This output assumes department 6 was inserted and no employee
has yet been assigned to it.


16. FOREIGN KEY CONSTRAINT TEST
------------------------------

Try to insert an employee with a department ID that does not exist.

INPUT
-----
Enter your choice: 2
Enter Employee ID: 110
Enter Employee Name: Suresh
Enter Salary: 42000
Enter Job Title: Tester
Enter Department ID: 999
Enter Manager ID: 101

EXPECTED OUTPUT
---------------
Employee could not be inserted because the department ID
does not exist in the parent table.

Also test:
- Updating an employee to a non-existing department.
- Deleting a department that is referenced by employees.
- Inserting an employee with an invalid manager ID.