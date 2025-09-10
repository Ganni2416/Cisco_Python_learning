employees = []

employee = ('bhanu', 22, 5000, True)
employees.append(employee)

employee = ('Mahesh', 21, 3000, True)
employees.append(employee)

employee = ('Vaishnavi', 42, 4000, True)
employees.append(employee)

print('after add all employees:', employees)

i = 0
search = 'vaishnavi'
index = -1
for emp in employees:
    if emp[0] == search:
        index = i
        break
    i += 1
if index == -1:
    print('Employee Not Found:')
else:
    search_employee = employees[index]
    print(search_employee)
    salary = float(input('salary:'))
    employee = (search_employee[0], search_employee[1], salary, search_employee[3])
    employees[index] = employee
print('After Search And Update:', employees)
employee = ('Dravid', 55, 6000, True)
employees.append(employee)
print('After add Employees:', employees)
employees.pop()
print('after delteing dravid:', employees)

position = 1
employees.pop(position)
print('after delete mahesh:', employees)

