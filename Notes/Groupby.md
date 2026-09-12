# Groupby
It is a SQL Clause used to divide rows into groups based on one or more columns so that aggregate functions can perform calculations independently for each group.  
It converts a large collections of rows into logical groups and allows us to calculate summary. 
```
select column_name,aggregatefunction(column_name) from tablename group by columnname;
```


1. WAQ to find total salary paid to each department.
```
select department,sum(salary) from employee_batch group by department;
+------------+-------------+
| department | sum(salary) |
+------------+-------------+
| IT         |   215001.20 |
| Finance    |   276001.10 |
| Sales      |   218001.45 |
+------------+-------------+
3 rows in set (0.01 sec)
```
2. WAQ to find no of employees in each department
```
select department,count(*) from employee_batch group by department;
+------------+----------+
| department | count(*) |
+------------+----------+
| IT         |        3 |
| Finance    |        4 |
| Sales      |        4 |
+------------+----------+
3 rows in set (0.00 sec)
```
Note: The above type of query is commonly used for 
1. no of orders per customer
2. no of products per category
3. no of students per course

## Count(*) VS Count(column)
Count(*) will count all the rows but count(column) ignores null 

3. WAQ to find avg salary of each department
```
select department,avg(salary) from employee_batch group by department;
+------------+--------------+
| department | avg(salary)  |
+------------+--------------+
| IT         | 71667.066667 |
| Finance    | 69000.275000 |
| Sales      | 54500.362500 |
+------------+--------------+
3 rows in set (0.01 sec)
```

4. WAQ to find lowest and highest salary in each department 

## group by with multiple columns
```
select department,job_role,count(*) from employee group by department,job_role;

the above example create a group for every unique combination of department and job role
```

```
select * from grp;
+---------+----------+--------+-----------------+----------+
| orderid | cname    | city   | productcategory | amount   |
+---------+----------+--------+-----------------+----------+
|     111 | deepika  | mumbai | electronics     | 15000.00 |
|     112 | rashmika | mumbai | clothes         |  5000.00 |
|     113 | kattappa | Indore | clothes         |  7000.00 |
|     114 | vaibhav  | Indore | electronics     | 12000.00 |
+---------+----------+--------+-----------------+----------+
```

1. WAQ to find total sales city wise

```
select city,sum(amount) from grp group by city;
+--------+-------------+
| city   | sum(amount) |
+--------+-------------+
| mumbai |    20000.00 |
| Indore |    19000.00 |
+--------+-------------+
2 rows in set (0.00 sec)
```
2. WAQ to find total sales for each city and productcategory
```
select city,productcategory,sum(amount) from grp group by city,productcategory;
+--------+-----------------+-------------+
| city   | productcategory | sum(amount) |
+--------+-----------------+-------------+
| mumbai | electronics     |    15000.00 |
| mumbai | clothes         |     5000.00 |
| Indore | clothes         |     7000.00 |
| Indore | electronics     |    12000.00 |
+--------+-----------------+-------------+
4 rows in set (0.00 sec)
```

## Group by with where clause
Where filters individual rows first then group by creates groups from the remaining groups. 
```
table -- where(filter rows)--- group by--aggregate funstions--result
```

1. WAQ to  find the average salary of employees in each department but consider only employees having more than 50k salary
```
select department,avg(salary) from employee_batch where salary>50000 group by department;
+------------+--------------+
| department | avg(salary)  |
+------------+--------------+
| IT         | 71667.066667 |
| Finance    | 69000.275000 |
| Sales      | 62500.175000 |
+------------+--------------+
3 rows in set (0.04 sec)
```
2. WAQ to find the no of employees in each department whose salary is greater than 50k.
```
select department,count(*) from employee_batch where salary>50000 group by department;
+------------+----------+
| department | count(*) |
+------------+----------+
| IT         |        3 |
| Finance    |        4 |
| Sales      |        2 |
+------------+----------+
3 rows in set (0.01 sec)
```
3. WAQ to find the highest salary in each department considering only active employees
```
select department,max(salary) from employee_batch where status="active" group by department;
+------------+-------------+
| department | max(salary) |
+------------+-------------+
| IT         |    85000.00 |
| Finance    |    82000.20 |
| Sales      |    70000.25 |
+------------+-------------+
3 rows in set (0.00 sec)
```
4. WAQ to find the no of active employees for each department and city
```
select department,city,count(*) from employee_batch where status="active" group by department,city;
+------------+--------+----------+
| department | city   | count(*) |
+------------+--------+----------+
| IT         | Pune   |        1 |
| Finance    | Delhi  |        1 |
| Sales      | Indore |        1 |
| Sales      | Mumbai |        2 |
| Finance    | Pune   |        1 |
| IT         | Delhi  |        1 |
| Finance    | Bhopal |        2 |
| IT         | NULL   |        1 |
| Sales      | Pune   |        1 |
+------------+--------+----------+
9 rows in set (0.00 sec)
```
5. WAQ to find department wise employees count who joined after jan 2025
```
select department,count(*) from employee_batch where join_date>='2025-01-01' group by department;
```

## Group by with order by
1. Find total salary of each department and display departments from highest total salary to lowest total salary
```
select department,sum(salary) as total_salary from employee_batch group by department order by total_salary desc;
+------------+--------------+
| department | total_salary |
+------------+--------------+
| Finance    |    276001.10 |
| Sales      |    218001.45 |
| IT         |    215001.20 |
+------------+--------------+
3 rows in set (0.01 sec)
```
2. WAQ to find no of employees in each department and display departments from highest count to lowest count
```
select department,count(*) as total_count from employee_batch group by department order by total_count desc;
+------------+-------------+
| department | total_count |
+------------+-------------+
| Finance    |           4 |
| Sales      |           4 |
| IT         |           3 |
+------------+-------------+
3 rows in set (0.00 sec)
```
3. WAQ to find top two departments based on total salary
```
select department,sum(salary) as total_salary from employee_batch group by department order by total_salary desc limit 2;
+------------+--------------+
| department | total_salary |
+------------+--------------+
| Finance    |    276001.10 |
| Sales      |    218001.45 |
+------------+--------------+
2 rows in set (0.00 sec)
```
* Can we use offset with group by - yeah we can 

4. WAQ to find highest salary in each department considering only active employees
```
select department,max(salary) from employee_batch where status='active' group by department;
```
5. WAQ to find no of active employees for each department and city
```
select department,city,count(*) from employee_batch where status="active" group by department,city
```

# Having 
Having is a sql clause used to filter groups created by the group by clause.  
Where clause filters individual rows whereas having clause filters groups.

1. WAQ to find departments having more than 2 employees
```
select department,count(*) from employee_batch group by department having count(*)>2;
+------------+----------+
| department | count(*) |
+------------+----------+
| IT         |        3 |
| Finance    |        4 |
| Sales      |        4 |
+------------+----------+
3 rows in set (0.02 sec)
```

## Where VS Having 
| WHERE | HAVING |
|---|---|
| Filters rows | Filters groups |
| Works before `GROUP BY` | Works after `GROUP BY` |
| Used with individual rows/columns | Commonly used with aggregate results |

Order :
table-where--filter rows---group by-----aggregate----having--- filter groups--order by--limit

1. WAQ to find departments where total_salary>2 lakhs
```
select department,sum(salary) from employee_batch group by department having sum(salary)>200000;
+------------+-------------+
| department | sum(salary) |
+------------+-------------+
| IT         |   215001.20 |
| Finance    |   276001.10 |
| Sales      |   218001.45 |
+------------+-------------+
3 rows in set (0.01 sec)
```
2. WAQ to find departments where employee count>2 and avg salary is greater than 15000?
```
select department,count(*),avg(salary) from employee_batch group by department having avg(salary)>50000 and count(*)>2;
+------------+----------+--------------+
| department | count(*) | avg(salary)  |
+------------+----------+--------------+
| IT         |        3 | 71667.066667 |
| Finance    |        4 | 69000.275000 |
| Sales      |        4 | 54500.362500 |
+------------+----------+--------------+
3 rows in set (0.01 sec)
```
3. WAQ to find departments having atleast 2 active employees
```
select department,count(*) from employee_batch where status="active" group by department having count(*)>=2;
```
4. WAQ to find Departments where no of active employees is atleast 5
```
select department,count(*) from employee_batch where status="active" group by department having count(*)>=5;
```

## Rules for Group by
1. selected normal column should be in group by.
```
select city,count(*) from employee_batch group by department;
ERROR 1055 (42000): Expression #1 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'batch18.employee_batch.city' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
```
2. if multiple columns are selected then put them in group by 
3. Aggregate functions are not required in group by 
```
select department,count(*) as total from employee_batch group by department,count(*);
error: Can't group on 'tota;'
```
4.  Use aggregate functions to summarize group data 
```
select department from employee_batch group by department;
+------------+
| department |
+------------+
| IT         |
| Finance    |
| Sales      |
+------------+
3 rows in set (0.01 sec)
```
5. Where clause must be first 
6. Having doesn't work without aggregate functions
7. Without group by having don't work
```
select sum(salary) from employee_batch having sum(salary)>50000;
```

# with roll up 
It is an extension of group by that automatically adds summary rows such as sub totals to the result.
```
select column1,aggregate(column2) from employee group by column1 with rollup;
```
```
select department,sum(salary) from employee_batch group by department with rollup;
+------------+-------------+
| department | sum(salary) |
+------------+-------------+
| Finance    |   276001.10 |
| IT         |   215001.20 |
| Sales      |   218001.45 |
| NULL       |   709003.75 |  Here Null is showing total of all 
+------------+-------------+
4 rows in set (0.01 sec)
```

```
select department,city from employee_batch group by department,city;
+------------+--------+
| department | city   |
+------------+--------+
| IT         | Pune   |
| Finance    | Delhi  |
| Sales      | Indore |
| Sales      | Mumbai |
| Finance    | Pune   |
| IT         | Delhi  |
| Finance    | Bhopal |
| IT         | NULL   |
| Sales      | Pune   |
+------------+--------+
9 rows in set (0.00 sec)
We can use group by without aggregate in that case it will give one row for each group
```
## Diff b/w distinct and group by 
