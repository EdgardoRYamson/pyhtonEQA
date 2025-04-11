def calculate_salary(hours_worked, hourly_rate, deductions):
    """
    Calculate gross and net salary based on working hours, hourly rate, and deductions.

    Parameters:
        hours_worked (float): Total hours worked.
        hourly_rate (float): Pay rate per hour.
        deductions (float): Total deductions.

    Returns:
        tuple: Gross salary and net salary.
    """
    gross_salary = hours_worked * hourly_rate
    

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
