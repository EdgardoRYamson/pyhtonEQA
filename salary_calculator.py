def calculate_salary(hours_worked, hourly_rate, deductions):
    # Calculate gross salary
    gross_salary = hours_worked * hourly_rate
    
    # Calculate net salary after deductions
    net_salary = gross_salary - deductions
    
    return gross_salary, net_salary

# Input details
print("Salary Calculator")
hours = float(input("Enter total working hours: "))
rate = float(input("Enter hourly rate: "))
deduction = float(input("Enter total deductions: "))

# Calculate salary
gross, net = calculate_salary(hours, rate, deduction)

# Display results
print("\nSalary Details:")
print(f"Gross Salary: {gross:.2f}")
print(f"Net Salary: {net:.2f}")
