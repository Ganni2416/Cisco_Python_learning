
#CRUD (Create, Read All | Read One, Update, Delete)
#Employee App - Inmem array - dict element 
employees = [] # [{'id':id,'name':name,'age':age,'salary':salary,'is_active':is_active}, ...]

def create_employee(employee):
    employees.append(employee)

def read_all_employee():
    return employees 

def read_by_id(emp_id):
    for employee in employees:
        if employee['id'] == emp_id:
            return employee 
    return None 

def update(emp_id, new_employee):#new_employee is update at emp_id
    global employees
    I = 0
    for employee in employees:
        if employee['id'] == emp_id:
            employees[I] = new_employee
            break 
        I += 1
    
def delete_employee(emp_id):
    global employees
    index = -1
    I = 0
    for employee in employees:
        if employee['id'] == emp_id:
            index = I
            break 
        I += 1
    if index != -1:
        employees.pop(index)
