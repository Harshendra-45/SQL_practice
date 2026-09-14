# Sub Query:  
A Subquery is a query written inside another Sql query.
```
-- 14/september/2026

mysql> CREATE TABLE subdepartment(deptid INT PRIMARY KEY, dname VARCHAR(20));
Query OK, 0 rows affected (1.49 sec)

mysql> DESC subdepartment;
+--------+-------------+------+-----+---------+-------+
| Field  | Type        | Null | Key | Default | Extra |
+--------+-------------+------+-----+---------+-------+
| deptid | int         | NO   | PRI | NULL    |       |
| dname  | varchar(20) | YES  |     | NULL    |       |
+--------+-------------+------+-----+---------+-------+
2 rows in set (0.01 sec)

mysql> INSERT INTO subdepartment VALUES(1,'HR'), (2,'IT'), (3,'finance');
Query OK, 3 rows affected (0.25 sec)
Records: 3  Duplicates: 0  Warnings: 0

mysql> SELECT * FROM subdepartment;
+--------+---------+
| deptid | dname   |
+--------+---------+
|      1 | HR      |
|      2 | IT      |
|      3 | finance |
+--------+---------+
3 rows in set (0.00 sec)


Another table


mysql> CREATE TABLE subemployee( eid INT PRIMARY KEY, ename VARCHAR(20), salary INT, deptid INT);
Query OK, 0 rows affected (0.33 sec)

mysql> DESC subemployee;
+--------+-------------+------+-----+---------+-------+
| Field  | Type        | Null | Key | Default | Extra |
+--------+-------------+------+-----+---------+-------+
| eid    | int         | NO   | PRI | NULL    |       |
| ename  | varchar(20) | YES  |     | NULL    |       |
| salary | int         | YES  |     | NULL    |       |
| deptid | int         | YES  |     | NULL    |       |
+--------+-------------+------+-----+---------+-------+
4 rows in set (0.01 sec)


mysql> INSERT INTO subemployee VALUES(101, 'amit', 3000, 1), (102, 'rahul', 50000, 2), (103, 'deepika', 6000, 3), (104, 'rashmika', 89000, 1), (105, 'katappa', 70000, 2);
Query OK, 5 rows affected (0.16 sec)
Records: 5  Duplicates: 0  Warnings: 0

mysql> SELECT * FROM subemployee;
+-----+----------+--------+--------+
| eid | ename    | salary | deptid |
+-----+----------+--------+--------+
| 101 | amit     |   3000 |      1 |
| 102 | rahul    |  50000 |      2 |
| 103 | deepika  |   6000 |      3 |
| 104 | rashmika |  89000 |      1 |
| 105 | katappa  |  70000 |      2 |
+-----+----------+--------+--------+
5 rows in set (0.00 sec)
```
## Types
1. Single row subquery :
A single row subquery returns exactly one row or one value, it is generally used with (=,<,>,<=,>=,<>).  

WAQ to find employee earning more than the avg salary?
```
without subquery:
select avg(salary) from subemployee;
+-------------+
| avg(salary) |
+-------------+
|  43600.0000 |
+-------------+
1 row in set (0.01 sec)

select * from subemployee where salary>43600;
+-----+----------+--------+--------+
| eid | ename    | salary | deptid |
+-----+----------+--------+--------+
| 102 | rahul    |  50000 |      2 |
| 104 | rashmika |  89000 |      1 |
| 105 | katappa  |  70000 |      2 |
+-----+----------+--------+--------+
3 rows in set (0.01 sec)

With subquery:
select * from subemployee where salary>(select avg(salary) from subemployee);
+-----+----------+--------+--------+
| eid | ename    | salary | deptid |
+-----+----------+--------+--------+
| 102 | rahul    |  50000 |      2 |
| 104 | rashmika |  89000 |      1 |
| 105 | katappa  |  70000 |      2 |
+-----+----------+--------+--------+
3 rows in set (0.00 sec)
```

WAQ to find employees earning exactly the maximum salary
```
select * from subemployee where salary=( select max(salary) from subemployee);
+-----+----------+--------+--------+
| eid | ename    | salary | deptid |
+-----+----------+--------+--------+
| 104 | rashmika |  89000 |      1 |
+-----+----------+--------+--------+
1 row in set (0.00 sec)
```

WAQ to find employees earning atleast the avg salary
```
select * from subemployee where salary>(select avg(salary) from subemployee);
```

WAQ to find employees whose salary is not equal to the minimum salary
```
select * from subemployee where salary<>(select min(salary) from subemployee);
+-----+----------+--------+--------+
| eid | ename    | salary | deptid |
+-----+----------+--------+--------+
| 102 | rahul    |  50000 |      2 |
| 103 | deepika  |   6000 |      3 |
| 104 | rashmika |  89000 |      1 |
| 105 | katappa  |  70000 |      2 |
+-----+----------+--------+--------+
4 rows in set (0.00 sec)
```

2. Multiple row subquery
A multiple row subquery returns more than one row, it is commonly used with (in,not in,any,some,all)

WAQ to find employees who are working in it or finance
```
mine
select * from subemployee as e inner join subdepartment as d where e.deptid=d.deptid and dname in ("it","finance");
select * from subemployee as e where dname in ("it","finance");
select * from subemployee as e inner join subdepartment as d where e.deptid=d.deptid and dname in ("it","finance");
+-----+---------+--------+--------+--------+---------+
| eid | ename   | salary | deptid | deptid | dname   |
+-----+---------+--------+--------+--------+---------+
| 102 | rahul   |  50000 |      2 |      2 | IT      |
| 103 | deepika |   6000 |      3 |      3 | finance |
| 105 | katappa |  70000 |      2 |      2 | IT      |
+-----+---------+--------+--------+--------+---------+
3 rows in set (0.01 sec)

select * from subemployee where deptid in(select deptid from subdepartment where dname="it" or dname="finance");
+-----+---------+--------+--------+
| eid | ename   | salary | deptid |
+-----+---------+--------+--------+
| 102 | rahul   |  50000 |      2 |
| 103 | deepika |   6000 |      3 |
| 105 | katappa |  70000 |      2 |
+-----+---------+--------+--------+
3 rows in set (0.01 sec)
```

WAQ to find employee who are not in it or finance;
```
select * from subemployee where deptid  not in(select deptid from subdepartment where dname="it" or dname="finance");
+-----+----------+--------+--------+
| eid | ename    | salary | deptid |
+-----+----------+--------+--------+
| 101 | amit     |   3000 |      1 |
| 104 | rashmika |  89000 |      1 |
+-----+----------+--------+--------+
2 rows in set (0.00 sec)
```
3. Multiple column subquery
It returns two or more columns
```
syntax
select col1,col2 from tablename where (col1,col2) in (select col1,col2 from tablename where condition );
```

WAQ to find the highest paid employee from each department 
```
select deptid,max(salary) from subemployee group by deptid;
+--------+-------------+
| deptid | max(salary) |
+--------+-------------+
|      1 |       89000 |
|      2 |       70000 |
|      3 |        6000 |
+--------+-------------+
3 rows in set (0.00 sec)

The above query is multiple column , multiple row subquery

SELECT ename, eid, deptid, salary
FROM subemployee
WHERE (deptid, salary) IN (
    SELECT deptid, MAX(salary)
    FROM subemployee
    GROUP BY deptid
);
+----------+-----+--------+--------+
| ename    | eid | deptid | salary |
+----------+-----+--------+--------+
| deepika  | 103 |      3 |   6000 |
| rashmika | 104 |      1 |  89000 |
| katappa  | 105 |      2 |  70000 |
+----------+-----+--------+--------+
```

WAQ to find employees who's salary is greater than any salary in dept 1
```
select * from subemployee where salary> any(select salary from subemployee where deptid=1);
+-----+----------+--------+--------+
| eid | ename    | salary | deptid |
+-----+----------+--------+--------+
| 102 | rahul    |  50000 |      2 |
| 103 | deepika  |   6000 |      3 |
| 104 | rashmika |  89000 |      1 |
| 105 | katappa  |  70000 |      2 |
+-----+----------+--------+--------+
4 rows in set (0.00 sec)
```

WAQ to find all the employees who's salary is greater than every employee working in dept2
```
select * from subemployee where salary> all(select salary from subemployee where deptid=2);
+-----+----------+--------+--------+
| eid | ename    | salary | deptid |
+-----+----------+--------+--------+
| 104 | rashmika |  89000 |      1 |
+-----+----------+--------+--------+
1 row in set (0.00 sec)
```

WAQ to find employees who earn less than every employee in the finance department
```
SELECT *
FROM subemployee
WHERE salary < ALL (
    SELECT salary
    FROM subemployee
    WHERE deptid = (
        SELECT deptid
        FROM subdepartment
        WHERE dname = 'finance'
    )
);

+-----+-------+--------+--------+
| eid | ename | salary | deptid |
+-----+-------+--------+--------+
| 101 | amit  |   3000 |      1 |
+-----+-------+--------+--------+
1 row in set (0.00 sec)
```



