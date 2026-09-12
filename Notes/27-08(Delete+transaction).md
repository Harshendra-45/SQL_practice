# Delete
Delete is a dml command used to remove existing records from a table. 
```
Delete from table_name where condition;
```
Where is not mandatory but without it all rows will be deleted. 
```
delete from employee_batch where id = 2;
```
1. WAQ to delete all the employees who belong to hr department. 
```
delete from employee_batch where department="hr";
```
2. WAQ to delete it employees having more than 3 years of experience.
```
delete from emplo2 where department="it" and experience>3;
```
3. WAQ to delete employees who are not from it or hr.
```
delete from emplo2 where department not in ("it","hr");
```
4. WAQ to delete employees who joined before 2020.
```
delete from emplo2 where join_date<'2020-01-01';
```
5. WAQ to delete the employees with the lowest salary.
```
delete from employee_batch order by salary limit 1;
```
6. WAQ to delete with highest salary.
```
delete from employee_batch order by  salary desc limit 1;
```
7. WAQ to delete lowest paid it employee.
```
delete from employee_batch where department="it" order by salary limit 1;
```
8. WAQ to delete it or hr employees whose salary is below 60k.
```
delete from employee_batch where department in ("it","hr") and salary<60000;
```

## Difference in Delete VS Truncate
1. Delete = DML | Truncate = DDL
2. Delete can use where | Cannot use where
3. Delete can delete selected data | It remove all data 
4. Can use conditions | No conditions
5. It can use order by , limit etc. | Cannot use anything 
6. It follows row-by-row deletion symantics | It deallocates table data more directly 
7. It can be rolled back when used within a transaction under appropriate transactional conditions. | It cannot be rolled back as it uses implicit commit 
8. Delete doesn't reset auto_increment | Truncate resets auto_increment, it means next time when we enter data again it starts from 1


## Delete VS Drop
1. Delete = DML | Drop = DDL
2. Delete remove rows | It removes database object itself(table)
3. After delete table structure remains | After drop table structure remove
4. In delete column, constraints and index will remain | But in drop all gets removed
5. Delete allows where | It doesn't allow where
6. In delete selected data gets deleted | But drop it is not possible to remove selected data.
7. Delete allows rollback | Drop is a ddl so implicitly gets committed and no rollback allowed.
8. Delete doesn't reset auto_increment | Drop deletes table so no auto_increment.

# TCL
Transaction control language are used to manage transactions in a db. A transaction is a group of SQL statements that should be treated as one logical unit of block .  
Common commands: 
1. Commit
2. rollback
3. savepoint
4. rollback to savepoint
5. release savepoint 
6. start transaction  

```
start transaction;
sql statement1;
sql statement2;
sql statement3;
commit;

or 
begin;
sql statements;
commit;
```

**Commit** permanently saves all changes made during the current transactions.

```
start transaction;
update accounts set balance=balance+2000 where accid=102;
select * from accounts;
rollback;
```

**Rollback**: rollback is used to undo changes made during the current transaction. 
```
start 
update 
rollback
update 
rollback ( no revert as transaction not started again)
```
**Savepoint**: A savepoint is a temporary checkpoint created inside a transaction. 
* It allows us to partially undo a transaction without undoing the entire transaction. 
```
start transaction
operation1;
operation2;
savepoint sp1;
operation3;
operation4;
rollback to sp1
```
The above syntax will undo the operation 3 and 4 . It will keep op 1 & 2 and it will keep the transaction active,which allows us to execute more SQL Statements. We can finally commit or rollback. 

Note: Rollback to savepoint doesn't end the transaction. 
```
create table orders(orderid int primary key,name varchar(20),pname varchar(20),amount decimal(10,2),orderstatus varchar(20));
insert into orders values(101,"Rahul","Laptop",50000,'pending'),(102,"amit","mobile",30000,'pending');
start transaction;
update orders set orderstatus="confirmed" where orderid=101;
savepoint orderconfirmed;
rollback to savepoint orderconfirmed;
update orders set amount=amount+500 where orderid = 101;
commit;
```

**Release Savepoint** : It is used to remove a savepoint from current transaction. 
```
release savepoint savepointname;
```
```
update orders set orderstatus="confirmed" where orderid=101;
savepoint orderconfirmed;
release savepoint orderconfirmed;
```

Note: if we perform rollback then entire transaction is cancelled and the savepoint is also gone , therefore if we use command rollback to sp spname then it will give error (savepoint spname doesn't exist).  
Same for commit   
