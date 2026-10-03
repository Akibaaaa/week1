emp_name = input("Employee name: ")
basic_salary = float(input("Basic salary: "))
transport_allowance = float(input("Transport Allowance: "))
food_allowance = float(input("Food Allowance: "))
Gross = basic_salary + transport_allowance + food_allowance
print("==========================================")
print("           EMPLOYEE PAYSLIP               ")
print("==========================================")
print(f'''Employee: {emp_name}
Basic Salary: {basic_salary}
Transport Allowance: {transport_allowance}
Food Allowance: {food_allowance}
------------------------------------------
Gross Salary: {Gross}''')
print("==========================================")
