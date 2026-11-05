
identification = input("Please enter the employee I.D")

employee_name = input("Please enter the employee full name: ")

status = input("Please enter the employee status: ")
if status == "fortnightly":
    hourly_rate = 550
elif status == "monthly":
    hourly_rate = 1200
else:
    print("Invalid employment status")

hours = int(input("Please enter the number of hours the employee worked: "))

gross_salary = hourly_rate * hours
print(f"Gross Salary: {gross_salary}")

NHT = gross_salary * 2/100
print(f"National Housing Trust: {NHT}")

PAYE = gross_salary * 25/100
print(f"Pay As You Earn: {PAYE}")

NIS = gross_salary * 2.5/100
print(f"National Insurance Scheme: {NIS}")

educational_tax = gross_salary * 2.25/100
print(f"Educational Tax: {educational_tax}")

total_deductions = NHT + PAYE + NIS + educational_tax
print(f"Total Deductions: {total_deductions}")

Net_salary = gross_salary - total_deductions 
print(f"Net Salary: {Net_salary}")

