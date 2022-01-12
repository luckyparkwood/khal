employee_file = open("cloudcall employees.txt", "r")
employee_list = (employee_file.readlines())

for employee in employee_list:
    print(employee_list.index(employee), " ", employee)



employee_file.close()
