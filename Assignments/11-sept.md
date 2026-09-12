QNO 1:
A company wants to manage its employees and their respective departments. Each employee must belong to a department. If a department is deleted, all employees in that department should also be removed automatically.
Tasks:
1. Create the Departments Table
Each department has a unique ID (DepartmentID).
The department name must be unique.
The department name cannot be NULL.
```
create table department(depid int primary key,depname varchar(20) unique not null);
```
2. Create the Employees Table
Each employee has a unique ID (EmployeeID).
Each employee has a name and salary, both cannot be NULL.
Each employee must be assigned to a department (DepartmentID), which is a FOREIGN KEY referencing Departments(DepartmentID).
If a department is deleted, all employees in that department should also be deleted.
```
create table employee(empid int primary key,empname varchar(25) not null,salary decimal(10,2) not null,depid int,foreign key(depid) references department(depid) on delete cascade);
```
3. Insert Sample Data
Insert at least 3 departments.
Insert at least 5 employees (make sure at least two employees belong to the same department).
```
insert into department values(1,"IT"),(2,"HR"),(3,"Finances");
insert into employee values(101,"Deepika",200000,1),(102,"Rashmika",300000,1),(103,"Bahubali",40000,2),(104,"Katappa",25000,3),(105,"Gabbar",150000,2);
```

4. Implement Query Constraints (Without Using JOIN)
Write a query to list all employees and their department names (without using JOIN).
Write a query to update an employee's department.
Try deleting a department and observe what happens to the employees under that department.
```
 select employee.empname,department.depname from employee,department where employee.depid=department.depid;
+----------+----------+
| empname  | depname  |
+----------+----------+
| Katappa  | Finances |
| Bahubali | HR       |
| Gabbar   | HR       |
| Deepika  | IT       |
| Rashmika | IT       |
+----------+----------+
5 rows in set (0.00 sec)

update employee set depid=3 where empid=101;

delete from department where depid=1;
```

QNO 2:-

A hospital wants to store patient records and their assigned doctors. If a doctor leaves, all related patient records should be deleted.

Tasks:
Create a Doctors table:
DoctorID (PRIMARY KEY, AUTO_INCREMENT)
DoctorName (NOT NULL)
Specialization (NOT NULL, UNIQUE)
```
create table doctors(docid int primary key auto_increment,docname varchar(20) not null,specialization varchar(20) not null unique);
```

Create a Patients table:
PatientID (PRIMARY KEY, AUTO_INCREMENT)
PatientName (NOT NULL)
DoctorID (FOREIGN KEY)
Insert sample data (at least 3 doctors and 5 patients).
```
create table patients(patid int primary key auto_increment, patname varchar(20) not null,docid int, foreign key(docid) references doctors(docid) on delete cascade);

insert into doctors(docname,specialization) values("Sakshi","neurologist"),("Neha","orthologist"),("Preetam","cardiologist");

insert into patients(patname,docid) values("Khushi",1),("Atba",3),("BJ",2);

mysql> select * from doctors;
+-------+---------+----------------+
| docid | docname | specialization |
+-------+---------+----------------+
|     1 | Sakshi  | neurologist    |
|     2 | Neha    | orthologist    |
|     3 | Preetam | cardiologist   |
+-------+---------+----------------+
3 rows in set (0.00 sec)

mysql> select * from patients;
+-------+---------+-------+
| patid | patname | docid |
+-------+---------+-------+
|     1 | Khushi  |     1 |
|     2 | Atba    |     3 |
|     3 | BJ      |     2 |
+-------+---------+-------+
3 rows in set (0.00 sec)
```

Delete a doctor and check if related patients are removed automatically.
```
mysql> delete from doctors where docid=2;
Query OK, 1 row affected (0.01 sec)

mysql> select * from patients;
+-------+---------+-------+
| patid | patname | docid |
+-------+---------+-------+
|     1 | Khushi  |     1 |
|     2 | Atba    |     3 |
+-------+---------+-------+
2 rows in set (0.00 sec)
```

Update a patient’s doctor to a new doctor.
```
mysql> update patients set docid=1 where patid=2;
Query OK, 1 row affected (0.02 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql> select * from patients;
+-------+---------+-------+
| patid | patname | docid |
+-------+---------+-------+
|     1 | Khushi  |     1 |
|     2 | Atba    |     1 |
+-------+---------+-------+
2 rows in set (0.00 sec)
```

QNO 3:
A library maintains a record of books and their authors. If an author is removed, their books should not be deleted, but their author information should be set to NULL.

Tasks:
Create an Authors table:
AuthorID (PRIMARY KEY, AUTO_INCREMENT)
AuthorName (NOT NULL, UNIQUE)
```
create table authors(autid int primary key auto_increment,autname varchar(20) not null unique);
```

Create a Books table:
BookID (PRIMARY KEY, AUTO_INCREMENT)
BookTitle (NOT NULL, UNIQUE)
AuthorID (FOREIGN KEY )
Insert sample data (at least 3 authors and 5 books).
```
create table books(bkid int primary key auto_increment,bktitle varchar(20) not null unique,autid int,foreign key(autid) references authors(autid));
insert into authors(autname) values("Shakespeare"),("Robert Frost"),("Harivansh Rai");

insert into books(bktitle,autid) values("The winters tale",1),("hamlet",1),("A boys will",2),("north of boston",2),("Madhushala",3);

mysql> select * from authors;
+-------+---------------+
| autid | autname       |
+-------+---------------+
|     3 | Harivansh Rai |
|     2 | Robert Frost  |
|     1 | Shakespeare   |
+-------+---------------+
3 rows in set (0.00 sec)

mysql> select * from books;
+------+------------------+-------+
| bkid | bktitle          | autid |
+------+------------------+-------+
|    1 | The winters tale |     1 |
|    2 | hamlet           |     1 |
|    3 | A boys will      |     2 |
|    4 | north of boston  |     2 |
|    5 | Madhushala       |     3 |
+------+------------------+-------+
5 rows in set (0.00 sec)
```
Delete an author and check if books remain, but the AuthorID is set to NULL.
```
update books set autid=null where bkid=5;
delete from authors where autid=3;
```
Update the author of a book to a new author.
```
mysql> update books set autid=2 where bkid=1;
```

QNO 4:
A university wants to track students' exam results. If a student is deleted, their results should also be deleted.
Tasks:
Create a Students table:
StudentID (PRIMARY KEY, AUTO_INCREMENT)
StudentName (NOT NULL)
```
create table students(sid int primary key auto_increment,sname varchar(20) not null);
```
Create an Exams table:
ExamID (PRIMARY KEY, AUTO_INCREMENT)
SubjectName (NOT NULL, UNIQUE)
```
create table exams(eid int primary key auto_increment,subname varchar(20) not null unique);
```
Create a Results table:
ResultID (PRIMARY KEY, AUTO_INCREMENT)
StudentID (FOREIGN key)
ExamID (FOREIGN KEY)
Score (NOT NULL, CHECK Score BETWEEN 0 AND 100)
```
create table results(rid int primary key auto_increment,sid int,eid int,score int not null check(0<score<100),foreign key(sid) references students(sid),foreign key(eid) references exams(eid));
```
Insert sample data (at least 3 students, 3 exams, and 5 results).
```
insert into students(sname) values("Aarav"),("priya"),("rohan");

insert into exams(subname) values("maths"),("Science"),("English");

insert into results(sid,eid,score) values(1,1,87),(1,2,67),(1,3,44),(2,1,54),(2,2,66),(2,3,98),(3,1,39),(3,2,90),(3,3,45);
```

Delete a student and check if their results are removed automatically.
```
No on delete in table structure
so 🫡
```


Update an exam’s subject name and observe the effect.
```
No effect
```
