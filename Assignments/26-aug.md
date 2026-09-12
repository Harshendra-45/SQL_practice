QNO 1:
Table Name: staff_update

| Column         | Data Type                      |
| -------------- | ------------------------------ |
| `staff_id`     | INT PRIMARY KEY AUTO_INCREMENT |
| `staff_name`   | VARCHAR(50)                    |
| `department`   | VARCHAR(30)                    |
| `city`         | VARCHAR(30)                    |
| `salary`       | DECIMAL(10,2)                  |
| `experience`   | INT                            |
| `age`          | INT                            |
| `joining_date` | DATE                           |
| `status`       | VARCHAR(20)                    |
===================================================

```
create table staff_update(id int primary key auto_increment,name varchar(50),department varchar(30),city varchar(30),salary decimal(10,2),experience int, age int,joining_date date,status varchar(20));
```

DATA:--
('Aarav', 'IT', 'Indore', 48000, 3, 26, '2022-04-15', 'Active'),
('Bhavna', 'HR', 'Bhopal', 56000, 5, 31, '2020-08-20', 'Active'),
('Chetan', 'Finance', 'Delhi', 62000, 7, 35, '2018-03-10', 'Active'),
('Divya', 'IT', 'Pune', 78000, 9, 38, '2016-11-05', 'Active'),
('Eshan', 'Sales', 'Indore', 51000, 4, 29, '2021-06-18', 'Inactive'),
('Farah', 'HR', NULL, 68000, 6, 34, '2019-01-25', 'Active');

```
insert into staff_update(name,department,city,salary,experoence,age,joining_date,status) values("aarav","it","indore",48000,3,26,'2022-04-15',"Active"),("Bhavna","Hr","Bhopal",56000,5,31,'2020-08-20',"Active"),("Chetan","Finance","Delhi",62000,7,35,'2018-03-10','Active'),('Divya', 'IT', 'Pune', 78000, 9, 38, '2016-11-05', 'Active'),('Eshan', 'Sales', 'Indore', 51000, 4, 29, '2021-06-18', 'Inactive'),('Farah', 'HR', NULL, 68000, 6, 34, '2019-01-25', 'Active');
```


Questions

Q1. Aarav's salary needs to be revised to ₹52,000. Update his salary using his employee ID.
```
update staff_update set salary=52000 where id=1;
```

Q2. Bhavna has been transferred to the Finance department in Indore. Update both her department and city.
```
update staff_update set city="Indore",department="Finance" where id = 2;
```

Q3. Give a ₹4,000 increment to employees whose salary is below ₹60,000, who have at least 3 years of experience, and who do not belong to Sales.
```
update staff_update set salary=salary+4000 where salary<60000 and department<>"hr" and experience>=3;
```

Q4. Give a ₹3,000 increment to employees who either belong to IT with at least 3 years of experience or belong to HR with at least 5 years of experience.
```
update staff_update set salary=salary+3000 where (department="it" and experience>=3) or (department="hr" and experience>=5);
```

Q5. Give a 10% increment to employees from IT or Finance whose current salary is below ₹70,000.
```
update staff_update set salary=salary*1.10 where department in ("it","finance") and salary<70000;
```

Q6. Give a ₹2,500 increment to employees who are neither from HR nor Sales and have between 5 and 8 years of experience.
```
update staff_update set salary=salary+2500 where department not in ("hr","sales") and experience between 5 and 8;
```

Q7. Give a ₹5,000 increment to employees whose salary is between ₹50,000 and ₹70,000, excluding Finance employees.
```
update staff_update set salary=salary+5000 where department<>"finance" and salary between 50000 and 70000;
```

Q8. Give a 7% increment to employees whose names start with either A or D.
```
update staff_update set salary=salary*1.07 where name like "a%" or "d%";
```

Q9. Farah's city is missing. Update her city to Mumbai without modifying employees whose city is already available.
```
update staff_update set city="Mumbai" where city is null;
```

Q10. Give a 10% increment to employees who joined before January 1, 2020 and whose salary is below ₹70,000.
```
update staff_update set salary=salary*1.10 where joining_date<'2020-01-01' and salary<70000;
```

Q11. For IT employees having at least 5 years of experience, increase salary by 8%, increase experience by 1 year, and change their status to Promoted.
```
update staff_update set salary=salary*1.08,experience=experience+1,status="Promoted" where department="it" and experience>=5;
```

Q12. Give a ₹6,000 increment to employees having at least 5 years of experience, salary below ₹75,000, and belonging to either HR or Finance.
```
update staff_update set salary=salary+6000 where department in ("HR","Finance") and salary<75000 and experience>=5;
```


Q13. Apply the following salary revisions in a single statement:

IT → 12%
HR → 9%
Finance → 8%
Sales → 5%

```
update staff_update set salary=
case 
    when department="it" then salary*1.12
    when department="hr" then salary*1.09
    when department="finance" then salary*1.08
    when department="sales" then salary*1.05
    else salary
end;
```

Q14. Apply salary increments according to experience:

8 or more years → 15%
5–7 years → 10%
3–4 years → 7%
Less than 3 years → 5%
```
update staff_update set salary=
case 
    when experience>=8 then salary*1.15
    when experience>=5 then salary*1.10
    when experience>=3 then salary*1.07
    else salary*1.05
end;
```


Q15. Apply these salary revisions in a single statement:

IT employees with at least 8 years → 18%
Other IT employees → 10%
HR employees with at least 6 years → 12%
Other HR employees → 7%
Finance employees → 8%
Sales employees → 5%
```
update staff_update set salary=
case 
    when department="it" and experience>=8 then salary*1.18
    when department="it"  then salary*1.10
    when department="hr" and experience>=6 then salary*1.12
    when department="hr"  then salary*1.07
    when department="finance" then salary*1.08
    when department="sales" then salary*1.05
    else salary
end;
```

Q16. Update the status of every employee according to salary:

₹75,000 or more → Senior
₹60,000–₹74,999 → Experienced
₹50,000–₹59,999 → Regular
Below ₹50,000 → Junior
```
update staff_update set status = 
case 
    when salary>=75000 then "Senior"
    when salary>=60000 then "Experienced"
    when salary>=50000 then "Regular"
    else "Junior"
end;
```
    

Q17. Display all employees with departments arranged in this business priority:

Finance → IT → HR → Sales

Do not change the actual department values.
```
select * from staff_update order by
case 
    when department='finance' then 1 
    when department='it' then 2 
    when department="hr" then 3 
    when department='sales' then 4
end;
```

Q18. Display all employees with departments arranged in this order:

IT → HR → Finance → Sales

Within each department, display the employee with the highest salary first.
```
select * from staff_update order by 
case
    when department='it' then 1 
    when department='hr' then 2 
    when department="finance" then 3 
    when department='sales' then 4
end,salary desc;
```

Q19. Display employees according to experience priority:

8+ years → 5–7 years → 3–4 years → below 3 years

```
select * from staff_update order by
case 
    when experience>=8 then 1
    when experience>=5 then 2
    when experience>=3 then 3
    else 4
end;
```

Q20. Give a ₹5,000 increment to only one employee. The employee must belong to IT or HR, have at least 3 years of experience, and earn less than ₹70,000. If multiple employees qualify, update only the lowest-paid employee.
```


Q21. Give a 10% increment to only one employee. The employee must be Active and have at least 5 years of experience. If multiple employees qualify, update only the highest-paid employee.

Q22. Give a ₹3,000 increment to only one employee who is neither from HR nor Sales and has at least 3 years of experience. If multiple employees qualify, update the lowest-paid employee.

Q23. Change the status to Promoted for only the highest-paid IT employee.

Q24. Give a 12% increment to employees who are either IT employees with at least 5 years of experience or Finance employees earning below ₹65,000. In addition, only Active employees earning below ₹80,000 should receive the increment.

Q25. Apply the following salary revision in one statement:

IT + 8 or more years → 18%
IT + 5–7 years → 12%
HR + at least 6 years → 10%
HR + less than 6 years → 7%
Finance + salary below ₹65,000 → 10%
Finance + salary ₹65,000 or above → 7%
Sales + at least 4 years → 6%
All remaining employees → 3%

Q26. Update both salary and status according to experience:

8+ years → salary +15%, status Promoted
5–7 years → salary +10%, status Eligible
3–4 years → salary +7%, status Regular
Below 3 years → salary +5%, status Junior

Q27. Change the status to Promoted for employees who have at least 6 years of experience, salary of at least ₹60,000, are Active, and belong to IT, HR, or Finance.

Q28. Employees belonging to IT, having at least 5 years of experience, and currently living in Pune or Delhi should receive a 10% salary increment, have their city changed to Bangalore, and their status changed to Transferred.

Q29. Give a ₹7,000 special increment to only one eligible employee. The employee must belong to IT, HR, or Finance, have at least 4 years of experience, be Active, and earn less than ₹75,000. If multiple employees qualify, update only the lowest-paid employee.
```

```

Q30. The company wants to perform an annual salary revision using one statement:

IT + experience >= 8 + salary >= ₹70,000 → 18%
IT + experience >= 5 → 12%
HR + experience >= 6 → 10%
HR + experience < 6 → 7%
Finance + salary < ₹65,000 → 10%
Finance + salary >= ₹65,000 → 7%
Sales + experience >= 4 → 6%
All remaining employees → 3%

Employees whose status is Inactive must not receive any increment.

Additionally, update the status based on the applicable increment:

15% or more → Promoted
10%–14.99% → Eligible
Below 10% → Under Review
```

```