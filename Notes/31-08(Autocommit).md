## Autocommit
Autocommit is a mysql setting that determines whether each sql statement is automatically committed as soon as it executes. 
* By default mysql usually has autocommit = 1 or autocommit=ON that means every successful transaction statement is automatically committed. 
```
select @@autocommit;
+--------------+
| @@autocommit |
+--------------+
|            1 |
+--------------+
1 row in set (0.00 sec)
```
```
mysql> show variables like 'autocommit';
+---------------+-------+
| Variable_name | Value |
+---------------+-------+
| autocommit    | ON    |
+---------------+-------+
1 row in set (0.02 sec)
```

## Autocommit=OFF
```
set autocommit = 0;
```
```
update anything
rollback 
if u want to save then commit instead of rollback
```

Note: If DDL commands are used they do autocommit, also when autocommit=0 so they wont be rolled back


## Difference between Commit and Autocommit 
1. Autocommit is a transaction setting while commit is a tcl command.
2. Autocommit controls automatic committing if it is ON then it will auto commit, if it is OFF then commit required while commit can be implicit or explicit.



