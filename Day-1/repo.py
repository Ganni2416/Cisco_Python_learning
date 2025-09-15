Employees=[] # [(Id,Name,Age,Salary,is_active)]

#  CRUD : CReate,Update,Read,Delete

def create_employee(employee):
    Employees.append(employee)
    
def read_all_employee():
    return Employees

def read_by_id(emp_id):
    for employee in Employees:
        if employee[0] == emp_id:
            return employee
    return None
def update(emp_id, new_employee):
    I = 0
    for employee in Employees:
        if employee[0] == emp_id:
            Employees[I] = new_employee
            break
        I += 1        
def delete_employee(emp_id):
    index = -1
    I = 0
    for employee in Employees:
        if employee[0] == emp_id:
            index = I
            break
        I += 1
    if index != -1:
        Employees.pop(index)
    if index != -1:
        Employees.pop(index)
