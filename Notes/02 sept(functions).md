# Function 
A function is a predefined operation that accepts one or more values as input, perform a specific operation and return a result
## Types of Functions 
In MYSQL Functions are classified into two types :
1. Single row(Scalar functions)
2. Aggregate Functions(Group functions)

### Single row /  Scalar Functions
It operates on individual rows and produce one result for each row.

**Types of Scalar functions**:
1. String functions
2. numeric functions
3. date and time 
4. conditonal functions
5. null handling functions
6. conversion functions

**String Functions**: They perform operations on character or string data.
* upper : shows data in upper case
```
select upper("deepika");
select name,upper(name) from student;
```
* concat : concatenate strings 
* lower : lower the string
* trim : used to remove white spaces around a string
* replace : replaces a value with another 
```
syntax: 
replace(whole term,oldvalue,new value)

select '123-456-789' as phone, replace('123-456-789',"-","") as new_phone;
+-------------+-----------+
| phone       | new_phone |
+-------------+-----------+
| 123-456-789 | 123456789 |
+-------------+-----------+
1 row in set (0.00 sec)

```
```
create database learn;
use learn;

create table customer(id int,name varchar(20),country varchar(20));

insert into customer values(1,"rahul","India"),(2,"sourabh","Usa"),(3,"luldeep","nepal"),(4,"Arfa","Pakistan"),(5,"anil","Africa");

select name, country,concat(name," ",country) as name_country,lower(name) as name_low,upper(country) as country_up from customer;
+---------+----------+---------------+----------+------------+
| name    | country  | name_country  | name_low | country_up |
+---------+----------+---------------+----------+------------+
| rahul   | India    | rahul India   | rahul    | INDIA      |
| sourabh | Usa      | sourabh Usa   | sourabh  | USA        |
| luldeep | nepal    | luldeep nepal | luldeep  | NEPAL      |
| Arfa    | Pakistan | Arfa Pakistan | arfa     | PAKISTAN   |
| anil    | Africa   | anil Africa   | anil     | AFRICA     |
+---------+----------+---------------+----------+------------+
5 rows in set (0.01 sec)

```

* len: returns length of the string data
 


### Aggregate Functions 
An Aggregate function performs a calculation on a set of rows and returns one summarized result, they are used in business report, sales reports, e-commerce analytics etc.   
Aggregate functions process on multiple rows.
1. Count :  It is used to count rows or non-null values. There are 3 forms available for this:
    * Count(*)
    * Count(column)
    * Count(distinct column)
**count(*)** : It count rows 
```
select count(*) from employees;
returns no of rows

insert into emplo2 values();
Query OK, 1 row affected (0.05 sec)

select count(*) from emplo2;
+----------+
| count(*) |
+----------+
|        2 |
+----------+
1 row in set (0.02 sec)

select * from emplo2;
+----+-------+--------+------------+----------+------------+------+------------+--------+
| id | name  | city   | department | salary   | experience | age  | join_date  | status |
+----+-------+--------+------------+----------+------------+------+------------+--------+
|  5 | Vikas | Bhopal | hr         | 90000.00 |          8 |   35 | 2018-03-12 | Active |
|  7 | NULL  | NULL   | NULL       |     NULL |       NULL | NULL | NULL       | NULL   |
+----+-------+--------+------------+----------+------------+------+------------+--------+
2 rows in set (0.00 sec)
```

**count(column)** : It counts non-null values in that column. 
```
select count(age) from emplo2;
+------------+
| count(age) |
+------------+
|          1 |
+------------+
1 row in set (0.00 sec)
```
Note: The difference b/w count(*) and count(age) is count(*) counts how many rows exist and count(age) counts how many employees have age value.

**count(distinct column)** : It counts unique non-null values.
```
select count(distinct city) from pystudent;
All unique values count will come
```

2. Sum : It calculates the total of numeric values.  
Sum ignores null value.
```
 select sum(salary) from employee_batch;
+-------------+
| sum(salary) |
+-------------+
|   709003.75 |
+-------------+
1 row in set (0.00 sec)
```

**SUM with WHERE**: Aggregate functions become more powerful when combined with filtering. 
```
select sum(salary) from employee_batch where department="it";
+-------------+
| sum(salary) |
+-------------+
|   215001.20 |
+-------------+
1 row in set (0.00 sec)
```
WAQ to give sum of all salaries above 50k
```
select sum(salary) from employee_batch where salary>50000;
+-------------+
| sum(salary) |
+-------------+
|   616002.65 |
+-------------+
1 row in set (0.01 sec)
```

3. Average(avg): Average calculates arithmetic mean. 
```
select avg(salary) from employee_batch;
+--------------+
| avg(salary)  |
+--------------+
| 64454.886364 |
+--------------+
1 row in set (0.00 sec)
```
```
mysql> select * from pystudent;
+------+----------+------+--------------+
| id   | name     | age  | city         |
+------+----------+------+--------------+
|    1 | Harsh    |   21 | Indore       |
|  100 | Anil     | NULL | Dewas        |
|  101 | Sahil    |   22 | Indore       |
|  102 | Abhishek |   22 | Double choki |
|  105 | Bhumi    |   22 | Indore       |
+------+----------+------+--------------+
5 rows in set (0.03 sec)

mysql> select avg(age) from pystudent;
+----------+
| avg(age) |
+----------+
|  21.7500 |
+----------+
1 row in set (0.00 sec)
Null gets excluded when average is calculated.
```

4. Min : Returns minimum values
```
select min(age) from pystudent;
```
 
5. Max : Returns Max value
```
select max(age) from pystudent;
```

```
all aggregate used together
select count(*) as totalemployee,sum(salary) as totalsalary,avg(salary) as avgsalary,min(salary) as minimum,max(salary) as maximum from employee_batch;
+---------------+-------------+--------------+----------+----------+
| totalemployee | totalsalary | avgsalary    | minimum  | maximum  |
+---------------+-------------+--------------+----------+----------+
|            11 |   709003.75 | 64454.886364 | 46000.70 | 85000.00 |
+---------------+-------------+--------------+----------+----------+
1 row in set (0.00 sec)
```

