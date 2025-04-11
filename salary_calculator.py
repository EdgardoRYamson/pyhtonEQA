def calculate_salary(hours_worked, hourly_rate, deductions):

    gross_salary = hours_worked * hourly_rate


    net_salary = gross_salary - deductions

    return gross_salary, net_salary


print("Salary Calculator")
hours = float(input("Enter total working hours: "))
rate = float(input("Enter hourly rate: "))
deduction = float(input("Enter total deductions: "))


gross, net = calculate_salary(hours, rate, deduction)


print("\nSalary Details:")
print(f"Gross Salary: {gross:.2f}")
print(f"Net Salary: {net:.2f}")
