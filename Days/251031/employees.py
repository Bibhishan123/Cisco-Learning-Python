employees = []

def add_employee(employee):
    employees.append(employee)

def search_employee(id):
    I=0
    for employee in employees:
        if employee[0]==id:
            return I
        I+=1
    
def update_employee(id, salary):
    index = search_employee(id)
    if index != -1:
        employee = employees[index]
        new_employee = (employee[0],employee[1],employee[2],salary)
        employee[index] = new_employee
    else:
        print("Employee not found")

def delete_employee(id):
    index = search_employee(id)
    if index != -1:
            employees.pop(index)
            print("Employee Deleted Successfully")
    else:
        print("Employee Not Found")

add_employee(101,'Pratik','software Engineer',56000)
add_employee(102,'Abhishek','software Automation Engineer',40000)
add_employee(103,'Rishabh','software Automation Engineer',99000)
add_employee(104,'Nihar','software Automation Engineer',99)
add_employee(105,'Divya','Business Analyst',45000)

print(employees)

emp_index = search_employee(104)
if emp_index !=-1:
    print('Searched employee:', search_employee[emp_index])
else:
    print('Employee Not Found')

update_employee(104,99200)
print(employees)

add_employee(106,'mahesh', 'python Trainer', 4200)
print(employees)
delete_employee(106)
print(employees)
