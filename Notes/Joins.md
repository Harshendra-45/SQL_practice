# Joins 
A join is used to combine rows from two or more tables based on related column or logical conditions.  
* In a properly designed relational database information is usually divided into multiple tables to avoid duplication and to fetch data from all these tables we require joins.
* Foreign key is not required for joins but companies usually prefers to add them. A join doesn't necessarily require a foreign key, a foreign key establish referential integrity whereas a join establish a relationship for a particular query
```
Syntax:
select coln1,coln2 from table1 join table2 on table1.coln=table2.coln;
```
Example:
```
select * from employee18;
+-------+----------+--------+
| empid | empname  | deptid |
+-------+----------+--------+
|   101 | deepika  |      1 |
|   103 | thapaji  |      3 |
|   104 | kanak    |      1 |
|   105 | kalu     |   NULL |
|   106 | rashmika |      4 |
|   107 | katappa  |   NULL |
+-------+----------+--------+
6 rows in set (0.00 sec)

 select * from department18;
+--------+-----------+
| deptid | deptname  |
+--------+-----------+
|      1 | hr        |
|      2 | marketing |
|      3 | finance   |
|      4 | sales     |
+--------+-----------+
4 rows in set (0.00 sec)


select employee18.empname,department18.deptname from employee18 join department18 on employee18.deptid=department18.deptid;
+----------+----------+
| empname  | deptname |
+----------+----------+
| deepika  | hr       |
| kanak    | hr       |
| thapaji  | finance  |
| rashmika | sales    |
+----------+----------+
4 rows in set (0.00 sec)

we can use alias 

select e.empname,d.deptname from employee18 as e join department18 as d on e.deptid=d.deptid;
```
Note: The ***ON** clause specify the join condition used to determine which rows from 2 or more tables are related and should be combined.It tells the database engine how rows from the participating tables should be matched in our case (on e.deptid=d.deptid), it means match an employee row with department row when the employee's department id = department's department id. 
```
employee-
department--
find matching rows---
combining matching rows----
generate result
```
```
select e.empname,d.deptname from employee18 as e join department18 as d on e.deptid<>d.deptid;
+----------+-----------+
| empname  | deptname  |
+----------+-----------+
| deepika  | sales     |
| deepika  | finance   |
| deepika  | marketing |
| thapaji  | sales     |
| thapaji  | marketing |
| thapaji  | hr        |
| kanak    | sales     |
| kanak    | finance   |
| kanak    | marketing |
| rashmika | finance   |
| rashmika | marketing |
| rashmika | hr        |
+----------+-----------+
12 rows in set (0.01 sec)
``` 
## Types of Joins
1. Inner Join: It returns only those rows for which a matching condition exists in both tables,By default join is inner join.
* order doesn't matter here bcoz it only fetches common data
```
select employee18.empname,department18.deptname from employee18 INNER join department18 on employee18.deptid=department18.deptid;
+----------+----------+
| empname  | deptname |
+----------+----------+
| deepika  | hr       |
| kanak    | hr       |
| thapaji  | finance  |
| rashmika | sales    |
+----------+----------+
4 rows in set (0.00 sec)
```
2. Left Join:  It returns all the rows from left table, matching rows from the right table.
```
Ex:
Display every employee along with their department name, if an employee is not assigned to any valid department still display that employee 
select e.empname,d.deptname from employee18 as e left join department18 as d on e.deptid=d.deptid;
+----------+----------+
| empname  | deptname |
+----------+----------+
| deepika  | hr       |
| thapaji  | finance  |
| kanak    | hr       |
| kalu     | NULL     |
| rashmika | sales    |
| katappa  | NULL     |
+----------+----------+
6 rows in set (0.06 sec)
```
```
select e.empname,d.deptname from department18 as d left join employee18 as e on e.deptid=d.deptid;
+----------+-----------+
| empname  | deptname  |
+----------+-----------+
| deepika  | hr        |
| kanak    | hr        |
| NULL     | marketing |
| thapaji  | finance   |
| rashmika | sales     |
+----------+-----------+
5 rows in set (0.01 sec)
```
Note : In left join all the records from left table are confirmed. 

3.  Right Join : It returns all rows from the right table matching rows from the left table, if no matching rows exist in the  left table then null values are returned for the left table columns.
```
select e.empname,d.deptname from department18 as d right join employee18 as e on e.deptid=d.deptid;
+----------+----------+
| empname  | deptname |
+----------+----------+
| deepika  | hr       |
| thapaji  | finance  |
| kanak    | hr       |
| kalu     | NULL     |
| rashmika | sales    |
| katappa  | NULL     |
+----------+----------+
6 rows in set (0.00 sec)
```

4. cross join: A cross join combines every row of the first table to every row of second table.
```
A = 3 rows, B = 4 rows , result = 12 rows 
```
```
Cross join is useful when we intentionally need all possible combinations between two sets of data, for example generate all product and color combinations, generate all students and subject combination, generate all size with products, generate all cities with delivery slots.

select e.empname,d.deptname from department18 as d cross join employee18 as e ;
+----------+-----------+
| empname  | deptname  |
+----------+-----------+
| deepika  | sales     |
| deepika  | finance   |
| deepika  | marketing |
| deepika  | hr        |
| thapaji  | sales     |
| thapaji  | finance   |
| thapaji  | marketing |
| thapaji  | hr        |
| kanak    | sales     |
| kanak    | finance   |
| kanak    | marketing |
| kanak    | hr        |
| kalu     | sales     |
| kalu     | finance   |
| kalu     | marketing |
| kalu     | hr        |
| rashmika | sales     |
| rashmika | finance   |
| rashmika | marketing |
| rashmika | hr        |
| katappa  | sales     |
| katappa  | finance   |
| katappa  | marketing |
| katappa  | hr        |
+----------+-----------+
24 rows in set (0.00 sec)
```
In cross join we do not use **on** condition bcoz it doesn't find matching rows.
```
select e.empname,d.deptname from department18 as d , employee18 as e ;
same cross join using comma syntax
```
```
EX 2:
create table product18(pid int primary key,pname varchar(20));

create table color18(colorid int primary key,colorname varchar(20));

insert into product18 values(101,"jeans"),(102,"T-shirt"),(103,"jacket");

insert into color18 values(1,"Black"),(2,"Red"),(3,"Blue");

select p.pname,c.colorname from product18 as p,color18 as c;
+---------+-----------+
| pname   | colorname |
+---------+-----------+
| jacket  | Black     |
| T-shirt | Black     |
| jeans   | Black     |
| jacket  | Red       |
| T-shirt | Red       |
| jeans   | Red       |
| jacket  | Blue      |
| T-shirt | Blue      |
| jeans   | Blue      |
+---------+-----------+
9 rows in set (0.00 sec)

select p.pname,c.colorname from product18 as p,color18 as c order by  pname,colorname asc;
+---------+-----------+
| pname   | colorname |
+---------+-----------+
| jacket  | Black     |
| jacket  | Blue      |
| jacket  | Red       |
| jeans   | Black     |
| jeans   | Blue      |
| jeans   | Red       |
| T-shirt | Black     |
| T-shirt | Blue      |
| T-shirt | Red       |
+---------+-----------+
9 rows in set (0.00 sec)
```

5. Self join : self join is a join in which a table is joined with itself,it means the same table plays two different roles.
```
select * from selfemployee;
+-------+---------+-----------+
| empid | empname | managerid |
+-------+---------+-----------+
|   101 | Deepika |      NULL |
|   102 | thapa   |       101 |
|   105 | Hello   |       105 |
+-------+---------+-----------+
3 rows in set (0.04 sec)

WAQ to display every employee along with their manager's name 
select e.empname as employee,m.empname as manager from selfemployee as e join selfemployee as m on e.managerid=m.empid;
+----------+---------+
| employee | manager |
+----------+---------+
| thapa    | Deepika |
| Hello    | Hello   |
+----------+---------+

WAQ to display every employee including employees who don't have a manager
left join

```
WAQ to give Full join  for employee18 and department18;
```
MySQL doesn't support full join but we can implement it by
select e.empname,d.deptname from employee18 as e left join department18 as d on  e.deptid=d.deptid 
UNION
select e.empname,d.deptname from employee18 as e right join department18 as d on  e.deptid=d.deptid;

+----------+-----------+
| empname  | deptname  |
+----------+-----------+
| deepika  | hr        |
| thapaji  | finance   |
| kanak    | hr        |
| kalu     | NULL      |
| rashmika | sales     |
| katappa  | NULL      |
| NULL     | marketing |
+----------+-----------+
7 rows in set (0.00 sec)
```










