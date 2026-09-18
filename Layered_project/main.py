from service.employee_service import Employee_Service
from model.employee import Employee
print("Welcome to our website")
service=Employee_Service()
# service.displayemployee()
employee=Employee(1750,"Harsh",900000)
service.add_employee(employee)

