from app.models import db, Employee

# CREATE
def create_employee(employee_data):
    employee = Employee(**employee_data)
    db.session.add(employee)
    db.session.commit()

# READ all
def read_all_employee():
    employees = Employee.query.all()
    return [e.to_dict() for e in employees]

# READ by ID
def read_by_id(emp_id):
    employee = Employee.query.get(emp_id)
    if employee:
        return employee.to_dict()
    return {"error": "Employee not found"}, 404

# UPDATE
def update(emp_id, employee_data):
    employee = Employee.query.get(emp_id)
    if not employee:
        return {"error": "Employee not found"}, 404
    for key, value in employee_data.items():
        setattr(employee, key, value)
    db.session.commit()

# DELETE
def delete_employee(emp_id):
    employee = Employee.query.get(emp_id)
    if not employee:
        return {"error": "Employee not found"}, 404
    db.session.delete(employee)
    db.session.commit()
