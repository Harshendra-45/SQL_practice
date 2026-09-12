# Update 
Update is a Dml command which is used to modify existing records in a table. 
```
update tablename set column1=value,column2=value......where condition;
In this syntax where is not mandatory but without where every row will be updated
```
```
update emplo2 set salary=50000 where id=1;
```
**Update Multiple Columns**:  
You can update multiple columns in the same statement.
```
update emplo2 set salary=20000,city="Bhopal",department='hr' where id=5;
```
**Update using comparison operator**:  
```
update emplo2 set salary = 55000 where salary<50000;
update emplo2 set salary = 90000 where experience=5;
```
**WAQ to give 5k increment to it employees having atleast 5 yr of experience**:
```
update emplo2 set salary=salary+5000 where department="it" and  experience>=5;
```
**WAQ to give increment of 3k to hr department or finance department**:
```
update emplo2 set salary=salary+3000 where department in ("hr","finance");
```
**WAQ to give increment 10k to all the employees outside hr and finance department**:
```
update emplo2 set salary=salary+10000 where department not in ("hr","finance");
```
**WAQ to increase 7k to all employees whose salary is between 60k-70k**:
```
update emplo2 set salary=salary+7000 where salary between 60000 and 70000;
```
**WAQ to move all the employees to it department whose name starts with a**:
```
update emplo2 set department="it" where name like "a%";
```
**WAQ to update all the employee cities to goa who do not have any city**:
```
update emplo2 set city="goa" where city is null;
```
**WAQ to give 10% increment to all the it employees**:
```
update emplo2 set salary=salary+0.10*salary where department="it";
```
**WAQ to give 15% increment to it employees having more than 5 years of experience and salary below 80000**:
```
update emplo2 set salary=salary*1.15 where department="it" and experience>=5 and salary<80000;
```
```
update emplo2 set salary=salary*1.15,experience=experience+1 where department="it" and experience>=5 and salary<80000;
```
**WAQ to give 10% increment to those employees who joined before 2020**:
```
update emplo2 set salary=salary*1.10 where join_date<'2020-01-01';
update emplo2 set salary=salary*1.10 where year(join_date)<'2020';

```
## Case statement in MYSQL
Case is a conditional expression in mysql used to return different values based on different conditions it works similar to if-else in programming language.
```
case 
    when condition1 then result1
    when condition2 then result2
    when condition3 then result3
    else result
end
```
Example:
```
select name,salary,
 case
    when salary>=80000 then "high"
    when salary>=50000 then "medium"
    else "low"
 end as salary_category from emplo2;
```
**Case with orderby**:  
It is useful when we want custom sorting instead of normal alphabetical,numerical sorting. 
```
select name,department,salary from emplo2 
order by 
case 
    when department="it" then 1
    when department="hr" then 2
    when department="finance" then 3
    when department="sales" then 4
    else 5
end;
```
**WAQ to give 10% increment to it department, 8% increment to hr and 7% to finance department**:
```
update emplo2 set salary = 
 case
     when department="it" then salary*1.10
     when department="hr" then salary*1.08
     when department="finance" then salary*1.07
     else salary
 end;
```
**WAQ to give increment of 15% whose experience is greater then 8 yrs, give increment of 10% whose experience is greater than 5 yrs and increment of 7% to experience greater than 3 yrs otherwise 5%**
```
update emplo2 set salary=
    case
        when experience>=8 then salary*1.15
        when experience>=5 then salary*1.10
        when experience>=3 then salary*1.07
        else salary=salary*1.05
    end;
```
----------------------------------------------------
**WAQ to set status of one hr employee to inactive**:
```
update emplo2 set status="Inactive" where department = "hr" limit 1;(limit 1 will update the first as per table it find)
```
**WAQ to give 5k increment to the lowest paid it employee**
```
update emplo2 set salary=salary+5000 where department="it" order by salary asc limit 1;
```
**WAQ to increase second highest paid employee of it by 10k**
```


