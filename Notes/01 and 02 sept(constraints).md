# Constraints
Constraints are rules/restrictions applied on a table based on our requirement.  
Constraints are classified in three groups.
1. Domain Integrity constraints (default,not null,check)
2. Entity Integrity constraints (unique,primary key)
3. Refrential Integrity constraints (foreign key)

* Constraints are primarily used for data integrity.

## Domain Integrity constraints 
### Not Null : 
It specify that column must contain a value.
```
create table staff(id int,name varchar(20) not null,salary decimal(20,2));
insert into staff(id,name , salary) values(101,null,50000);
    ERROR 1048 (23000): Column 'name' cannot be null
insert into staff(id,name , salary) values(101,"null",50000); A null is in string so it accepts. 
insert into staff(id,name , salary) values(101,"",50000); valid 
```
Note : Null doesn't mean 0 or "" or "null". Null means unknown value or missing value or not available value. 

The not null constraint is also applied during update. 

### Unique 
The unique constrints ensures that a column cannot contain duplicate values. 
```
create table employee2(id int,email varchar(20) unique);
insert into employee2 values(102,"dipu@gmail.com");
Query OK, 1 row affected (0.02 sec)

mysql> insert into employee2 values(102,"dipu@gmail.com");
ERROR 1062 (23000): Duplicate entry 'dipu@gmail.com' for key 'employee2.email'
```

**unique constraint on multiple columns** :
```
mysql> insert into employee1 values(101,991,4444);
Query OK, 1 row affected (0.02 sec)

mysql> insert into employee1 values(101,991,5555);
Query OK, 1 row affected (0.01 sec)

mysql> insert into employee1 values(101,992,4444);
Query OK, 1 row affected (0.01 sec)

mysql> insert into employee1 values(101,991,5555);
ERROR 1062 (23000): Duplicate entry '991-5555' for key 'employee1.uk_dept'

```
from the above example it is clear that the combinations should be unique. 

### Unique vs Not null
1. unique prevents duplicate values but not null prevents missing values 
like multiple null's can be inserted for a unique values as null means unavailable.
```
create table employee20(id int, email varchar(20) unique);
insert into employee20(id) values(1010);
insert into employee20(id) values(10101);
select * from employee20;
+-------+-------+
| id    | email |
+-------+-------+
|  1010 | NULL  |
| 10101 | NULL  |
+-------+-------+
2 rows in set (0.00 sec)

```
from the above example it is clear that email cannot be duplicated, but null handling is different from ordinary value.   
If a application requires every employee to have an email and that should be unique. 
```
create table employee19(id int,email varchar(20) unique not null);
```

### Unique VS Primary key
1.  primary key uniquely identify row values while Unique prevents duplicates. 
2.  primary key cannot contain null while unique can contain null. 
3. One table can have only one primary key but a table can have multiple unique values.
```
create table employee21(id int primary key,email varchar(20) unique, mobile varchar(20) unique);
Query OK, 0 rows affected (0.10 sec)

mysql> desc employee21;
+--------+-------------+------+-----+---------+-------+
| Field  | Type        | Null | Key | Default | Extra |
+--------+-------------+------+-----+---------+-------+
| id     | int         | NO   | PRI | NULL    |       |
| email  | varchar(20) | YES  | UNI | NULL    |       |
| mobile | varchar(20) | YES  | UNI | NULL    |       |
+--------+-------------+------+-----+---------+-------+
3 rows in set (0.00 sec)
create table employee31(id int primary key,email varchar(20) primary key, mobile varchar(20) unique);
ERROR 1068 (42000): Multiple primary key defined
```
4. Primary key is used as main row identifier but unique is used for alternate candidate key. 

### Difference b/w Primary key and Unique + not null
Primary key will be only one per table.  
But we can define multiple columns as unique + not null


## Check 
Check constraint is a domain constraint used to restrict the values that can be inserted into or updated in a column based on specified condition.  
Check constraint ensures that data stored in a column satisfies a particular condition.
```
syntax: 
create table tablename( col_name datatype check(condition));
example:
create table adults(id int, name varchar(20),age int check(age>=18));
insert into adults values(1,"Anil",5);
    ERROR 3819 (HY000): Check constraint 'adults_chk_1' is violated.
insert into adults values(1,"Anil",55);
```
```
create table employees25(id int,name varchar(20),dno int check(dno in(10,20,30)));

insert into employees25 values(101,"deepika",40);
ERROR 3819 (HY000): Check constraint 'employees25_chk_1' is violated.

insert into employees25 values(101,"deepika",10);
Query OK, 1 row affected (0.02 sec)

insert into employees25(id,name) values(101,"deepika"); Null inserted as null is a different case and check doesn't handle it
Query OK, 1 row affected (0.01 sec)

select * from employees25;
+------+---------+------+
| id   | name    | dno  |
+------+---------+------+
|  101 | deepika |   10 |
|  101 | deepika | NULL |
+------+---------+------+
2 rows in set (0.00 sec)

To prevent this
use 
create table employee8(id int,name varchar(20),dno int check(dno in(10,20,30)) not null);
```

**Check with multiple conditions** : 
It can contain multiple conditions using operators.
```
create table employee89(id int,name varchar(20),age int,salary decimal(10,2),check(age>=18 and salary>=10000));

insert into employee89 values(101,"deepika",19,9000);
ERROR 3819 (HY000): Check constraint 'employee89_chk_1' is violated.

insert into employee89 values(101,"deepika",21,91000);
Query OK, 1 row affected (0.01 sec)
```
Suppose we want marks of student must be in a range 0 to 100.
```
create table student27(rollno int, name varchar(20),marks int check(marks between 0 and 100));
```
Note : Check constraint checks new insertions but also checks updated value. 

## Column level and Table level Constraints
Column level: 
The condition is written directly with column.  
used when condition relates to one column. 

Table level :
The condition is defined separately.  
Useful when condition involves multiple columns. 

### Naming a check constraint 
In Industry level Database design giving constraints meaningful name is a good practice.
```
create table employee(id int,name varchar(20),age int,constraint chk_employee_age check(age>=18))
```

## Diff B/W Check and Not Null



# Default Constraint 
It provides a value automatically when the user doesn't supply one. 
```
create table employee(id int primary key ,name varchar(20),status varchar(20) default 'active');

desc employee;
+--------+-------------+------+-----+---------+-------+
| Field  | Type        | Null | Key | Default | Extra |
+--------+-------------+------+-----+---------+-------+
| id     | int         | NO   | PRI | NULL    |       |
| name   | varchar(20) | YES  |     | NULL    |       |
| status | varchar(20) | YES  |     | active  |       |
+--------+-------------+------+-----+---------+-------+
3 rows in set (0.03 sec)

insert into employee(id,name) values(101,"deepika");
```
```
create table product(pid int,pname varchar(20),price int default 0);
```

## Default with date-time 
with the help of default we can automatically record the creation time.
```
create table employee(id int,name varchar(20),created_at datetime default current_timestamp);
insert into employee(id,name) values(101,"deepika");
```

**Not null and default**: 
```
create table employee100(id not null default 1, name varchar(20));

insert into employee100(name) values("deepika"),("rashmika");

select * from employee;
+----+----------+
| id | name     |
+----+----------+
|  1 | deepika  |
|  1 | rashmika |
+----+----------+
2 rows in set (0.00 sec)
```

```
create table employee(id int,name varchar(20),not null(id));
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'not null(id))' at line 1
Note: Not null constraint cannot be defined at table level 
```

**Check and Default**:
```
create table employee101(id int,name varchar(20),dno int default 10 check(dno in (10,20,30)));
```

## H.W use default not null and check constraints for a table 

