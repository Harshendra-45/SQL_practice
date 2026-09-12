CASE STUDY: Hospital Management & Appointment System


============================================================
1. BUSINESS SCENARIO
============================================================

A private hospital wants to develop a MySQL database to manage its daily operations.

The hospital has departments, doctors, patients, appointments, prescriptions and
medicines.

A patient can visit the hospital multiple times. Every visit is recorded as an
appointment between a patient and a doctor.

Each doctor belongs to a department.

After an appointment, the doctor may create a prescription. A prescription can
contain multiple medicines.

The hospital also wants the database to maintain historical records wherever
required.

Your task is to analyze the business requirements and design the database.


============================================================
2. DEPARTMENT DATA
============================================================

department_id | department_name | floor_no
------------------------------------------------
101           | Cardiology       | 3
102           | Neurology        | 4
103           | Orthopedics      | 2
104           | Dermatology      | 1


============================================================
3. DOCTOR DATA
============================================================

doctor_id | doctor_name      | specialization | department_id
----------------------------------------------------------------
201       | Dr. Rajesh Sharma| Cardiologist   | 101
202       | Dr. Neha Verma   | Neurologist    | 102
203       | Dr. Amit Jain    | Orthopedic     | 103
204       | Dr. Priya Singh  | Dermatologist  | 104
205       | Dr. Karan Mehta  | Cardiologist   | 101


============================================================
4. PATIENT DATA
============================================================

patient_id | patient_name  | gender | city
------------------------------------------------
301        | Rahul Verma   | Male   | Indore
302        | Sneha Sharma  | Female | Bhopal
303        | Amit Patel    | Male   | Indore
304        | Pooja Gupta   | Female | Ujjain
305        | Rohan Jain    | Male   | Dewas
306        | Neha Patel    | Female | Indore


============================================================
5. MEDICINE DATA
============================================================

medicine_id | medicine_name | manufacturer       | price
----------------------------------------------------------
401         | Paracetamol   | ABC Pharma         | 30
402         | Azithromycin  | XYZ Pharma         | 120
403         | Pantoprazole  | MedLife            | 80
404         | Amoxicillin   | HealthCare Pharma  | 150
405         | Ibuprofen     | ABC Pharma         | 60
406         | Cetirizine    | MedLife            | 45


============================================================
6. APPOINTMENT
============================================================

The hospital wants to maintain appointment information.

Each appointment belongs to:
- One patient
- One doctor
- One department

Therefore, the APPOINTMENT table will contain MULTIPLE FOREIGN KEYS.

Required columns:

appointment_id
appointment_date
appointment_time
patient_id
doctor_id
department_id
status


The following data must be inserted:

appointment_id | date       | time  | patient_id | doctor_id | department_id | status
---------------------------------------------------------------------------------------
501             | 2026-09-01 | 10:00 | 301        | 201       | 101           | Completed
502             | 2026-09-01 | 11:00 | 302        | 202       | 102           | Completed
503             | 2026-09-02 | 09:30 | 303        | 203       | 103           | Completed
504             | 2026-09-02 | 12:00 | 304        | 204       | 104           | Cancelled
505             | 2026-09-03 | 10:30 | 301        | 205       | 101           | Completed
506             | 2026-09-03 | 11:30 | 305        | 203       | 103           | Completed
507             | 2026-09-04 | 09:00 | 306        | 201       | 101           | Scheduled
508             | 2026-09-04 | 14:00 | 302        | 202       | 102           | Scheduled


============================================================
7. PRESCRIPTION
============================================================

After an appointment, a doctor can create a prescription.

Each prescription belongs to:
- One appointment
- One patient
- One doctor

Required columns:

prescription_id
prescription_date
appointment_id
patient_id
doctor_id
remarks


Data:

prescription_id | date       | appointment_id | patient_id | doctor_id | remarks
--------------------------------------------------------------------------------
601             | 2026-09-01 | 501            | 301        | 201       | BP observation
602             | 2026-09-01 | 502            | 302        | 202       | Migraine treatment
603             | 2026-09-02 | 503            | 303        | 203       | Knee pain
604             | 2026-09-03 | 505            | 301        | 205       | Heart checkup
605             | 2026-09-03 | 506            | 305        | 203       | Back pain


============================================================
8. PRESCRIPTION_MEDICINE
============================================================

One prescription can contain multiple medicines.

One medicine can be used in multiple prescriptions.

Therefore, this is a MANY-TO-MANY relationship.

Create a bridge table:

prescription_medicine

Required columns:

prescription_id
medicine_id
dosage
duration_days
quantity

Use a COMPOSITE PRIMARY KEY:

PRIMARY KEY (prescription_id, medicine_id)


Data:

prescription_id | medicine_id | dosage | duration_days | quantity
-----------------------------------------------------------------
601             | 401         | 1-0-1  | 5             | 10
601             | 403         | 1-0-0  | 5             | 5
602             | 403         | 1-0-0  | 7             | 7
602             | 406         | 0-0-1  | 5             | 5
603             | 405         | 1-0-1  | 5             | 10
603             | 403         | 1-0-0  | 5             | 5
604             | 401         | 1-0-1  | 3             | 6
604             | 403         | 1-0-0  | 3             | 3
605             | 405         | 1-0-1  | 7             | 14


============================================================
9. RELATIONSHIPS TO IDENTIFY
============================================================

Identify and implement the following relationships:

1. Department -> Doctor

2. Patient -> Appointment

3. Doctor -> Appointment

4. Department -> Appointment

5. Appointment -> Prescription

6. Patient -> Prescription

7. Doctor -> Prescription

8. Prescription -> Prescription_Medicine

9. Medicine -> Prescription_Medicine


IMPORTANT:

Do not simply create the tables randomly.

Analyze which table is the PARENT and which table is the CHILD.


============================================================
10. ON DELETE BUSINESS REQUIREMENTS
============================================================

You must choose the correct ON DELETE action based on the following
business scenarios.


SCENARIO A - DEPARTMENT CLOSED
--------------------------------

Department 104 (Dermatology) is closed permanently.

However, doctors who worked in that department should NOT be deleted.

Their department_id should become NULL.

Requirement:

Department -> Doctor

Use an appropriate ON DELETE action so that:

Doctor remains
department_id becomes NULL


SCENARIO B - DOCTOR LEAVES THE HOSPITAL
-----------------------------------------

Doctor 203 leaves the hospital.

The hospital wants to retain historical appointment records.

Therefore, deleting the doctor must NOT delete the appointments.

The doctor reference in existing appointments should become NULL.

Requirement:

Doctor -> Appointment

Use:

ON DELETE SET NULL


SCENARIO C - TEST PATIENT IS DELETED
-------------------------------------

Patient 306 is test/demo data and management wants to permanently
remove this patient.

Appointments belonging to this test patient should also be removed.

Requirement:

Patient -> Appointment

Use:

ON DELETE CASCADE


SCENARIO D - APPOINTMENT IS DELETED
------------------------------------

Appointment 501 is removed from the system.

Any prescription created specifically for that appointment should
also be removed.

Requirement:

Appointment -> Prescription

Use:

ON DELETE CASCADE


SCENARIO E - PRESCRIPTION IS DELETED
-------------------------------------

Prescription 601 is deleted.

Its records from prescription_medicine should automatically be removed.

Requirement:

Prescription -> Prescription_Medicine

Use:

ON DELETE CASCADE


SCENARIO F - MEDICINE IS IN USE
--------------------------------

Medicine 406 is already being used in existing prescriptions.

The hospital wants to protect historical prescription data.

Therefore, a medicine that is referenced by prescription_medicine
should NOT be deleted.

Requirement:

Medicine -> Prescription_Medicine

Use an appropriate action such as:

ON DELETE RESTRICT

Students must explain why ON DELETE CASCADE would be dangerous
in this situation.


============================================================
11. ON UPDATE CASCADE
============================================================

The hospital wants to change some department IDs during a data migration.

For example:

101 -> 1001
102 -> 1002
103 -> 1003
104 -> 1004

When a department ID changes, related foreign key values should
automatically change.

For example:

department.department_id
101 -> 1001

The related values in:

doctor.department_id
appointment.department_id

should automatically change from:

101 -> 1001

Requirement:

Use ON UPDATE CASCADE wherever appropriate.

Students must demonstrate this using an UPDATE statement.


============================================================
12. ON UPDATE SET NULL
============================================================

The hospital also wants to test a different update behavior.

Suppose doctor ID 203 is changed to 250 during an administrative
migration.

For a relationship configured with ON UPDATE SET NULL, the old
doctor reference in child records should become NULL rather than
automatically changing to 250.

Demonstrate:

UPDATE doctor
SET doctor_id = 250
WHERE doctor_id = 203;

Then check the related child records.

Expected behavior for the relationship configured with
ON UPDATE SET NULL:

Old doctor reference -> NULL

Students must explain the difference between:

ON UPDATE CASCADE
and
ON UPDATE SET NULL


============================================================
13. REQUIRED TASKS
============================================================

TASK 1
------

Create a database named:

hospital_management


TASK 2
------

Create all required tables:

1. department
2. doctor
3. patient
4. appointment
5. medicine
6. prescription
7. prescription_medicine
```
create table department(depid int primary key,depname varchar(20),floor_no int);

create table doctor(docid int primary key,docname varchar(20),specialization varchar(30),depid int,foreign key(depid) references department(depid) on delete set null on update cascade);

create table patient(patid int primary key, patname varchar(50),gender varchar(20),city varchar(20));

create table medicine(medid int primary key,medname varchar(50),manufacturer varchar(60),price int);

create table appointment(appid int primary key,date date,time time,patid int,docid int,depid int,status varchar(20), foreign key(patid) references patient(patid) on delete cascade on update cascade,foreign key(docid) references doctor(docid) on delete set null on update set null,foreign key(depid) references department(depid) on delete cascade on update cascade);

create table prescription(priid int primary key,pri_date date,appid int,patid int,docid int,remarks varchar(200), foreign key(appid) references appointment(appid) on delete cascade on update cascade,foreign key(patid) references patient(patid) on delete cascade on update cascade,foreign key(docid) references doctor(docid) on delete set null on update set null);

create table prescription_medicine(prescid int, medid int,dosage varchar(20),duration int,quantity int, primary key(prescid,medid),foreign key(prescid) references prescription(priid) on delete cascade on update cascade, foreign key(medid) references medicine(medid) on delete restrict on update cascade);
```



TASK 3
------

Identify the PRIMARY KEY of every table.


TASK 4
------

Identify every FOREIGN KEY.


TASK 5
------

Implement all relationships correctly.


TASK 6
------

For every FOREIGN KEY, decide and implement the appropriate:

ON DELETE
ON UPDATE


TASK 7
------

Insert all the given data.

```
insert into department values(101,"cardiology",3),(102,"Neurology",4),(103,"orthopedics",2),(104,"Dermatology",1);

insert into doctor values(201,"DR. Rajesh Sharma","Cardiologist",101),(202,"Dr. Neha Verma","Neurologist",102),(203,"DR. Amit Jain","Orthopedic",103),(204,"Dr. Priya Singh","Dermatologist",104),(205,"Dr. Karan Mehta","Cardiologist",101);

insert into patient values(301,"Rahul verma","Male","Indore"),(302,"Sneha Sharma","Female","Bhopal"),(303,"amit patel","male","Indore"),(304,"Pooja Gupta","female","Ujjain"),(305,"Rohan jain","Male","Dewas"),(306,"Neha patel","Female","Indore");

insert into medicine values(401,"paracetamol","ABC Pharma",30),(402,"Azithromycin","XYZ pharma",120),(403,"Pantoprazole","Medlife",80),(404,"Amoxicillin","Healthcare pharma",150),(405,"Ibuprofen","ABC Pharma",60),(406,"Cetirizine","Medlife",45);

insert into appointment values(501,"2026-09-01","10:00",301,201,101,"Completed"),(502,"2026-09-01","11:00", 302,202,102,"Completed"),(503,'2026-09-02','09:30',303,203, 103, "Completed"),(504,"2026-09-02","12:00", 304,204,104,"Cancelled"),(505,"2026-09-03","10:30", 301, 205, 101,"Completed"),(506,"2026-09-03","11:30", 305,203,103,"Completed"),(507,"2026-09-04","09:00",306,201,101,"Scheduled"),(508,"2026-09-04","14:00",302,202,102,"Scheduled");

INSERT INTO prescription
(priid, pri_date, appid, patid, docid, remarks)
VALUES
(601, '2026-09-01', 501, 301, 201, 'BP observation'),
(602, '2026-09-01', 502, 302, 202, 'Migraine treatment'),
(603, '2026-09-02', 503, 303, 203, 'Knee pain'),
(604, '2026-09-03', 505, 301, 205, 'Heart checkup'),
(605, '2026-09-03', 506, 305, 203, 'Back pain');

INSERT INTO prescription_medicine
(prescid, medid, dosage, duration, quantity)
VALUES
(601, 401, '1-0-1', 5, 10),
(601, 403, '1-0-0', 5, 5),
(602, 403, '1-0-0', 7, 7),
(602, 406, '0-0-1', 5, 5),
(603, 405, '1-0-1', 5, 10),
(603, 403, '1-0-0', 5, 5),
(604, 401, '1-0-1', 3, 6),
(604, 403, '1-0-0', 3, 3),
(605, 405, '1-0-1', 7, 14);


```
TASK 8
------

Display every table using:

SELECT * FROM table_name;
```
select * from department;
+-------+-------------+----------+
| depid | depname     | floor_no |
+-------+-------------+----------+
|   101 | cardiology  |        3 |
|   102 | Neurology   |        4 |
|   103 | orthopedics |        2 |
|   104 | Dermatology |        1 |
+-------+-------------+----------+
4 rows in set (0.00 sec)

select * from doctor;
+-------+-------------------+----------------+-------+
| docid | docname           | specialization | depid |
+-------+-------------------+----------------+-------+
|   201 | DR. Rajesh Sharma | Cardiologist   |   101 |
|   202 | Dr. Neha Verma    | Neurologist    |   102 |
|   203 | DR. Amit Jain     | Orthopedic     |   103 |
|   204 | Dr. Priya Singh   | Dermatologist  |   104 |
|   205 | Dr. Karan Mehta   | Cardiologist   |   101 |
+-------+-------------------+----------------+-------+
5 rows in set (0.00 sec)

select * from patient;
+-------+--------------+--------+--------+
| patid | patname      | gender | city   |
+-------+--------------+--------+--------+
|   301 | Rahul verma  | Male   | Indore |
|   302 | Sneha Sharma | Female | Bhopal |
|   303 | amit patel   | male   | Indore |
|   304 | Pooja Gupta  | female | Ujjain |
|   305 | Rohan jain   | Male   | Dewas  |
|   306 | Neha patel   | Female | Indore |
+-------+--------------+--------+--------+
6 rows in set (0.00 sec)

 select * from medicine;
+-------+--------------+-------------------+-------+
| medid | medname      | manufacturer      | price |
+-------+--------------+-------------------+-------+
|   401 | paracetamol  | ABC Pharma        |    30 |
|   402 | Azithromycin | XYZ pharma        |   120 |
|   403 | Pantoprazole | Medlife           |    80 |
|   404 | Amoxicillin  | Healthcare pharma |   150 |
|   405 | Ibuprofen    | ABC Pharma        |    60 |
|   406 | Cetirizine   | Medlife           |    45 |
+-------+--------------+-------------------+-------+
6 rows in set (0.00 sec)


select * from appointment;
+-------+------------+----------+-------+-------+-------+-----------+
| appid | date       | time     | patid | docid | depid | status    |
+-------+------------+----------+-------+-------+-------+-----------+
|   501 | 2026-09-01 | 10:00:00 |   301 |   201 |   101 | Completed |
|   502 | 2026-09-01 | 11:00:00 |   302 |   202 |   102 | Completed |
|   503 | 2026-09-02 | 09:30:00 |   303 |   203 |   103 | Completed |
|   504 | 2026-09-02 | 12:00:00 |   304 |   204 |   104 | Cancelled |
|   505 | 2026-09-03 | 10:30:00 |   301 |   205 |   101 | Completed |
|   506 | 2026-09-03 | 11:30:00 |   305 |   203 |   103 | Completed |
|   507 | 2026-09-04 | 09:00:00 |   306 |   201 |   101 | Scheduled |
|   508 | 2026-09-04 | 14:00:00 |   302 |   202 |   102 | Scheduled |
+-------+------------+----------+-------+-------+-------+-----------+
8 rows in set (0.00 sec)

 select * from prescription;
+-------+------------+-------+-------+-------+--------------------+
| priid | pri_date   | appid | patid | docid | remarks            |
+-------+------------+-------+-------+-------+--------------------+
|   601 | 2026-09-01 |   501 |   301 |   201 | BP observation     |
|   602 | 2026-09-01 |   502 |   302 |   202 | Migraine treatment |
|   603 | 2026-09-02 |   503 |   303 |   203 | Knee pain          |
|   604 | 2026-09-03 |   505 |   301 |   205 | Heart checkup      |
|   605 | 2026-09-03 |   506 |   305 |   203 | Back pain          |
+-------+------------+-------+-------+-------+--------------------+
5 rows in set (0.00 sec)

select * from prescription_medicine;
+---------+-------+--------+----------+----------+
| prescid | medid | dosage | duration | quantity |
+---------+-------+--------+----------+----------+
|     601 |   401 | 1-0-1  |        5 |       10 |
|     601 |   403 | 1-0-0  |        5 |        5 |
|     602 |   403 | 1-0-0  |        7 |        7 |
|     602 |   406 | 0-0-1  |        5 |        5 |
|     603 |   403 | 1-0-0  |        5 |        5 |
|     603 |   405 | 1-0-1  |        5 |       10 |
|     604 |   401 | 1-0-1  |        3 |        6 |
|     604 |   403 | 1-0-0  |        3 |        3 |
|     605 |   405 | 1-0-1  |        7 |       14 |
+---------+-------+--------+----------+----------+
9 rows in set (0.00 sec)


```
TASK 9
------

Test INVALID FOREIGN KEY.

Try inserting a child record using a parent ID that does not exist.

Example:

patient_id = 999

Observe the error and explain why MySQL rejected the record.
```
insert into doctor values(206,"Dr. Harsh","All rounder",5);
ERROR 1452 (23000): Cannot add or update a child row: a foreign key constraint fails (`11sepcs`.`doctor`, CONSTRAINT `doctor_ibfk_1` FOREIGN KEY (`depid`) REFERENCES `department` (`depid`) ON DELETE SET NULL ON UPDATE CASCADE)

INSERT INTO appointment
    -> (appid, date, time, patid, docid, depid, status)
    -> VALUES
    -> (509, '2026-09-05', '10:00:00', 999, 201, 101, 'Scheduled');
ERROR 1452 (23000): Cannot add or update a child row: a foreign key constraint fails (`11sepcs`.`appointment`, CONSTRAINT `appointment_ibfk_1` FOREIGN KEY (`patid`) REFERENCES `patient` (`patid`) ON DELETE CASCADE ON UPDATE CASCADE)
```



TASK 10
-------

Test ON DELETE CASCADE.

Delete a patient having appointments.

Check the appointment table before and after deletion.

Explain what happened.
```
mysql> select * from appointment;
+-------+------------+----------+-------+-------+-------+-----------+
| appid | date       | time     | patid | docid | depid | status    |
+-------+------------+----------+-------+-------+-------+-----------+
|   501 | 2026-09-01 | 10:00:00 |   301 |   201 |   101 | Completed |
|   502 | 2026-09-01 | 11:00:00 |   302 |   202 |   102 | Completed |
|   503 | 2026-09-02 | 09:30:00 |   303 |   203 |   103 | Completed |
|   504 | 2026-09-02 | 12:00:00 |   304 |   204 |   104 | Cancelled |
|   505 | 2026-09-03 | 10:30:00 |   301 |   205 |   101 | Completed |
|   506 | 2026-09-03 | 11:30:00 |   305 |   203 |   103 | Completed |
|   507 | 2026-09-04 | 09:00:00 |   306 |   201 |   101 | Scheduled |
|   508 | 2026-09-04 | 14:00:00 |   302 |   202 |   102 | Scheduled |
+-------+------------+----------+-------+-------+-------+-----------+
8 rows in set (0.00 sec)

t
mysql> delete from patient where patid=306;
Query OK, 1 row affected (0.02 sec)

mysql> select * from appointment;
+-------+------------+----------+-------+-------+-------+-----------+
| appid | date       | time     | patid | docid | depid | status    |
+-------+------------+----------+-------+-------+-------+-----------+
|   501 | 2026-09-01 | 10:00:00 |   301 |   201 |   101 | Completed |
|   502 | 2026-09-01 | 11:00:00 |   302 |   202 |   102 | Completed |
|   503 | 2026-09-02 | 09:30:00 |   303 |   203 |   103 | Completed |
|   504 | 2026-09-02 | 12:00:00 |   304 |   204 |   104 | Cancelled |
|   505 | 2026-09-03 | 10:30:00 |   301 |   205 |   101 | Completed |
|   506 | 2026-09-03 | 11:30:00 |   305 |   203 |   103 | Completed |
|   508 | 2026-09-04 | 14:00:00 |   302 |   202 |   102 | Scheduled |
+-------+------------+----------+-------+-------+-------+-----------+
7 rows in set (0.00 sec)
```


TASK 11
-------

Test ON DELETE SET NULL.

Delete a doctor.

Check the appointment table.

Verify that the appointment remains but doctor_id becomes NULL.
```
mysql> select * from appointment;
+-------+------------+----------+-------+-------+-------+-----------+
| appid | date       | time     | patid | docid | depid | status    |
+-------+------------+----------+-------+-------+-------+-----------+
|   501 | 2026-09-01 | 10:00:00 |   301 |   201 |   101 | Completed |
|   502 | 2026-09-01 | 11:00:00 |   302 |   202 |   102 | Completed |
|   503 | 2026-09-02 | 09:30:00 |   303 |   203 |   103 | Completed |
|   504 | 2026-09-02 | 12:00:00 |   304 |   204 |   104 | Cancelled |
|   505 | 2026-09-03 | 10:30:00 |   301 |   205 |   101 | Completed |
|   506 | 2026-09-03 | 11:30:00 |   305 |   203 |   103 | Completed |
|   508 | 2026-09-04 | 14:00:00 |   302 |   202 |   102 | Scheduled |
+-------+------------+----------+-------+-------+-------+-----------+
7 rows in set (0.00 sec)

mysql> select * from doctor;
+-------+-------------------+----------------+-------+
| docid | docname           | specialization | depid |
+-------+-------------------+----------------+-------+
|   201 | DR. Rajesh Sharma | Cardiologist   |   101 |
|   202 | Dr. Neha Verma    | Neurologist    |   102 |
|   203 | DR. Amit Jain     | Orthopedic     |   103 |
|   204 | Dr. Priya Singh   | Dermatologist  |   104 |
|   205 | Dr. Karan Mehta   | Cardiologist   |   101 |
+-------+-------------------+----------------+-------+
5 rows in set (0.00 sec)

mysql> delete from doctor where docid=205;
Query OK, 1 row affected (0.02 sec)

mysql> select * from doctor;
+-------+-------------------+----------------+-------+
| docid | docname           | specialization | depid |
+-------+-------------------+----------------+-------+
|   201 | DR. Rajesh Sharma | Cardiologist   |   101 |
|   202 | Dr. Neha Verma    | Neurologist    |   102 |
|   203 | DR. Amit Jain     | Orthopedic     |   103 |
|   204 | Dr. Priya Singh   | Dermatologist  |   104 |
+-------+-------------------+----------------+-------+
4 rows in set (0.00 sec)

mysql> select * from appointment;
+-------+------------+----------+-------+-------+-------+-----------+
| appid | date       | time     | patid | docid | depid | status    |
+-------+------------+----------+-------+-------+-------+-----------+
|   501 | 2026-09-01 | 10:00:00 |   301 |   201 |   101 | Completed |
|   502 | 2026-09-01 | 11:00:00 |   302 |   202 |   102 | Completed |
|   503 | 2026-09-02 | 09:30:00 |   303 |   203 |   103 | Completed |
|   504 | 2026-09-02 | 12:00:00 |   304 |   204 |   104 | Cancelled |
|   505 | 2026-09-03 | 10:30:00 |   301 |  NULL |   101 | Completed |
|   506 | 2026-09-03 | 11:30:00 |   305 |   203 |   103 | Completed |
|   508 | 2026-09-04 | 14:00:00 |   302 |   202 |   102 | Scheduled |
+-------+------------+----------+-------+-------+-------+-----------+
```


TASK 12
-------

Test ON DELETE RESTRICT.

Try deleting a medicine that is referenced by
prescription_medicine.

Observe the error.

Explain why MySQL rejected the deletion.
```
mysql> select * from prescription_medicine;
+---------+-------+--------+----------+----------+
| prescid | medid | dosage | duration | quantity |
+---------+-------+--------+----------+----------+
|     601 |   401 | 1-0-1  |        5 |       10 |
|     601 |   403 | 1-0-0  |        5 |        5 |
|     602 |   403 | 1-0-0  |        7 |        7 |
|     602 |   406 | 0-0-1  |        5 |        5 |
|     603 |   403 | 1-0-0  |        5 |        5 |
|     603 |   405 | 1-0-1  |        5 |       10 |
|     604 |   401 | 1-0-1  |        3 |        6 |
|     604 |   403 | 1-0-0  |        3 |        3 |
|     605 |   405 | 1-0-1  |        7 |       14 |
+---------+-------+--------+----------+----------+
9 rows in set (0.00 sec)

mysql>
mysql> select * from medicine;
+-------+--------------+-------------------+-------+
| medid | medname      | manufacturer      | price |
+-------+--------------+-------------------+-------+
|   401 | paracetamol  | ABC Pharma        |    30 |
|   402 | Azithromycin | XYZ pharma        |   120 |
|   403 | Pantoprazole | Medlife           |    80 |
|   404 | Amoxicillin  | Healthcare pharma |   150 |
|   405 | Ibuprofen    | ABC Pharma        |    60 |
|   406 | Cetirizine   | Medlife           |    45 |
+-------+--------------+-------------------+-------+
6 rows in set (0.00 sec)

mysql> delete from medicine where medid=401;
ERROR 1451 (23000): Cannot delete or update a parent row: a foreign key constraint fails (`11sepcs`.`prescription_medicine`, CONSTRAINT `prescription_medicine_ibfk_2` FOREIGN KEY (`medid`) REFERENCES `medicine` (`medid`) ON DELETE RESTRICT ON UPDATE CASCADE)
```


TASK 13
-------

Test ON UPDATE CASCADE.

Change a department primary key.

Verify that the related foreign keys are automatically updated.
```
mysql> select * from appointment;
+-------+------------+----------+-------+-------+-------+-----------+
| appid | date       | time     | patid | docid | depid | status    |
+-------+------------+----------+-------+-------+-------+-----------+
|   501 | 2026-09-01 | 10:00:00 |   301 |   201 |   101 | Completed |
|   502 | 2026-09-01 | 11:00:00 |   302 |   202 |   102 | Completed |
|   503 | 2026-09-02 | 09:30:00 |   303 |   203 |   103 | Completed |
|   504 | 2026-09-02 | 12:00:00 |   304 |   204 |   104 | Cancelled |
|   505 | 2026-09-03 | 10:30:00 |   301 |  NULL |   101 | Completed |
|   506 | 2026-09-03 | 11:30:00 |   305 |   203 |   103 | Completed |
|   508 | 2026-09-04 | 14:00:00 |   302 |   202 |   102 | Scheduled |
+-------+------------+----------+-------+-------+-------+-----------+

mysql> select * from department;
+-------+-------------+----------+
| depid | depname     | floor_no |
+-------+-------------+----------+
|   101 | cardiology  |        3 |
|   102 | Neurology   |        4 |
|   103 | orthopedics |        2 |
|   104 | Dermatology |        1 |
+-------+-------------+----------+
4 rows in set (0.00 sec)

mysql> update department set depid=105 where depid=101;
Query OK, 1 row affected (0.02 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql> select * from appointment;
+-------+------------+----------+-------+-------+-------+-----------+
| appid | date       | time     | patid | docid | depid | status    |
+-------+------------+----------+-------+-------+-------+-----------+
|   501 | 2026-09-01 | 10:00:00 |   301 |   201 |   105 | Completed |
|   502 | 2026-09-01 | 11:00:00 |   302 |   202 |   102 | Completed |
|   503 | 2026-09-02 | 09:30:00 |   303 |   203 |   103 | Completed |
|   504 | 2026-09-02 | 12:00:00 |   304 |   204 |   104 | Cancelled |
|   505 | 2026-09-03 | 10:30:00 |   301 |  NULL |   105 | Completed |
|   506 | 2026-09-03 | 11:30:00 |   305 |   203 |   103 | Completed |
|   508 | 2026-09-04 | 14:00:00 |   302 |   202 |   102 | Scheduled |
+-------+------------+----------+-------+-------+-------+-----------+
7 rows in set (0.00 sec)
```


TASK 14
-------

Test ON UPDATE SET NULL.

Change a doctor primary key.

Verify that the configured child foreign key becomes NULL.
```
 select * from doctor;
+-------+-------------------+----------------+-------+
| docid | docname           | specialization | depid |
+-------+-------------------+----------------+-------+
|   201 | DR. Rajesh Sharma | Cardiologist   |   105 |
|   202 | Dr. Neha Verma    | Neurologist    |   102 |
|   203 | DR. Amit Jain     | Orthopedic     |   103 |
|   204 | Dr. Priya Singh   | Dermatologist  |   104 |
+-------+-------------------+----------------+-------+
4 rows in set (0.00 sec)

mysql> update doctor set docid=210 where docid=204;
Query OK, 1 row affected (0.02 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql> select * from doctor;
+-------+-------------------+----------------+-------+
| docid | docname           | specialization | depid |
+-------+-------------------+----------------+-------+
|   201 | DR. Rajesh Sharma | Cardiologist   |   105 |
|   202 | Dr. Neha Verma    | Neurologist    |   102 |
|   203 | DR. Amit Jain     | Orthopedic     |   103 |
|   210 | Dr. Priya Singh   | Dermatologist  |   104 |
+-------+-------------------+----------------+-------+
4 rows in set (0.00 sec)

mysql> select * from appointment;
+-------+------------+----------+-------+-------+-------+-----------+
| appid | date       | time     | patid | docid | depid | status    |
+-------+------------+----------+-------+-------+-------+-----------+
|   501 | 2026-09-01 | 10:00:00 |   301 |   201 |   105 | Completed |
|   502 | 2026-09-01 | 11:00:00 |   302 |   202 |   102 | Completed |
|   503 | 2026-09-02 | 09:30:00 |   303 |   203 |   103 | Completed |
|   504 | 2026-09-02 | 12:00:00 |   304 |  NULL |   104 | Cancelled |
|   505 | 2026-09-03 | 10:30:00 |   301 |  NULL |   105 | Completed |
|   506 | 2026-09-03 | 11:30:00 |   305 |   203 |   103 | Completed |
|   508 | 2026-09-04 | 14:00:00 |   302 |   202 |   102 | Scheduled |
+-------+------------+----------+-------+-------+-------+-----------+
7 rows in set (0.00 sec)
```



============================================================
14. IMPORTANT QUESTIONS TO ANSWER
============================================================

Answer the following questions in your submission.

1. Why does the appointment table contain multiple foreign keys?

2. Which tables are parent tables and which are child tables?

3. What is the relationship between Patient and Appointment?

4. What is the relationship between Doctor and Appointment?

5. What is the relationship between Prescription and Medicine?

6. Why is prescription_medicine required?

7. Why is prescription_medicine using a composite primary key?

8. Why should deleting a doctor NOT delete historical appointments?

9. Why is ON DELETE SET NULL suitable for Department -> Doctor?

10. Why is ON DELETE CASCADE suitable for Patient -> Appointment
    in the given test-data scenario?

11. Why can ON DELETE CASCADE be dangerous for Medicine ->
    Prescription_Medicine?

12. What is the difference between ON DELETE CASCADE and
    ON DELETE SET NULL?

13. What is the difference between ON UPDATE CASCADE and
    ON UPDATE SET NULL?

14. What happens if you try to insert a child record with a
    non-existing parent ID?

15. What happens if you try to delete a parent record when
    ON DELETE RESTRICT is configured?


============================================================
15. SUBMISSION REQUIREMENTS
============================================================

Your submission must contain:

1. Database creation command
2. CREATE TABLE statements
3. PRIMARY KEY definitions
4. FOREIGN KEY definitions
5. ON DELETE definitions
6. ON UPDATE definitions
7. INSERT statements
8. SELECT * output for all tables
9. Invalid FK test
10. ON DELETE CASCADE test
11. ON DELETE SET NULL test
12. ON DELETE RESTRICT test
13. ON UPDATE CASCADE test
14. ON UPDATE SET NULL test
15. Answers to all theory questions


============================================================
GOOD LUCK!