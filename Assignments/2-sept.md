MYSQL STRING FUNCTIONS ASSIGNMENT
Scenario

A company wants to manage and analyze employee information using MySQL. The HR department needs to prepare different employee reports by formatting employee names, processing email addresses, extracting specific parts of employee information, removing unwanted spaces, and creating employee summaries.

You are given the following table and employee data. Write appropriate SELECT queries to perform the required operations.

Table Name: employee_string
Column	Data Type	Constraint
emp_id	INT	PRIMARY KEY, AUTO_INCREMENT
emp_name	VARCHAR(50)	NOT NULL
email	VARCHAR(100)	NOT NULL
department	VARCHAR(30)	NOT NULL
designation	VARCHAR(50)	NOT NULL
city	VARCHAR(30)	NOT NULL
phone	VARCHAR(15)	NOT NULL
DATA
('  Rahul Sharma  ', 'rahul.sharma@gmail.com', 'it', 'software developer', 'Indore', '9876543210'),
('Priya Verma', 'priya.verma@yahoo.com', 'hr', 'hr executive', 'Bhopal', '9876501234'),
('  Amit Patel', 'amit.patel@gmail.com', 'finance', 'account executive', 'Indore', '9123456780'),
('Neha Singh  ', 'neha.singh@company.com', 'marketing', 'marketing manager', 'Mumbai', '9988776655'),
('Rohit Jain', 'rohit.jain@gmail.com', 'it', 'team leader', 'Pune', '9090909090'),
('  Sneha Gupta ', 'sneha.gupta@yahoo.com', 'sales', 'sales executive', 'Delhi', '9012345678'),
('Vikas Yadav', 'vikas.yadav@gmail.com', 'finance', 'senior accountant', 'Jaipur', '9345678901'),
('Anjali Mehta', 'anjali.mehta@company.com', 'hr', 'hr manager', 'Indore', '9765432109'),
('  Karan Joshi  ', 'karan.joshi@gmail.com', 'it', 'database administrator', 'Bhopal', '8899776655'),
('Meena Kapoor', 'meena.kapoor@yahoo.com', 'sales', 'sales manager', 'Mumbai', '9001122334');
QUESTIONS
Q1.

The HR department wants to display all employee names in capital letters for an official employee report.

Q2.

The company wants all department names to be displayed in small letters for standardization.

Q3.

HR wants to know the length of each employee's name.

Display the employee name along with its length.

Q4.

The HR report should display employee names in the following format:

Employee: Rahul Sharma
Employee: Priya Verma

Create this output for every employee.

Q5.

HR wants to display only the first 5 characters of each employee's name.

Q6.

Some employee names contain unnecessary spaces before or after the name.

Display all employee names after removing the unwanted spaces.

Q7.

The company wants to replace the Gmail domain with the company's domain in the displayed email addresses.

For example:

rahul.sharma@gmail.com

should be displayed as:

rahul.sharma@company.com

Do not modify the original table data.

Q8.

HR wants to create a temporary employee code using the first 3 characters of the employee's name.

Display the employee name along with the generated code.

Q9.

For privacy purposes, the company wants to display only the last 4 digits of each employee's phone number.

Q10.

The HR department wants to display the employee's location in the following format:

Indore-IT
Bhopal-HR
Mumbai-Marketing

Combine the city and department using - between them.

Q11.

For a testing purpose, the IT department wants to display every employee's name in reverse order.

Q12.

The IT department wants to find the position of the @ symbol in every employee's email address.

Display the email address along with the position.

Combined Questions
Q13.

HR wants to create an official employee report in the following format:

RAHUL SHARMA - SOFTWARE DEVELOPER

Both the employee name and designation should appear in capital letters.

Q14.

Before generating the final report, HR wants to remove unwanted spaces from employee names and then display the cleaned names in capital letters.

Q15.

The company wants a final employee summary in the following format:

RAHUL SHARMA | SOFTWARE DEVELOPER | INDORE | 3210

The report should contain:

Employee name without unwanted spaces and in capital letters
Designation in capital letters
City in capital letters
Last 4 digits of phone number
| as separator between all values

Condition: Do not modify the original table data. Use only SELECT queries for all questions.