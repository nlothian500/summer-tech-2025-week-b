employee_count = 0
combined_gross = 0 
combined_NHT = 0
combined_PAYE = 0
combined_NIS = 0
combined_education_tax = 0
combined_deductions = 0
combined_net_salary = 0


while True:
    employee_id = input("Please enter the employee I.D")

    employee_name = input("Please enter the employee full name: ")

    while True:
        employment_status = input("Please enter the employee status: ")
        if employment_status == "fortnightly":
            hourly_rate = 550
            break
        elif employment_status == "monthly":
            hourly_rate = 1200
            break
        else:
            print("Invalid employment status try again")
            continue
                
    hours_work = int(input("Please enter the number of hours the employee worked: "))
    while hours_work < 0:
        print("Invalid hours the hours cannot be negative")
        hours_work = int(input("Please enter the number of hours the employee worked: "))

    gross_salary = hourly_rate * hours_work
    print(f"Gross Salary: ${gross_salary:.2f}")

    NHT = gross_salary * 2/100
    print(f"National Housing Trust: ${NHT:.2f}")

    PAYE = gross_salary * 25/100
    print(f"Pay As You Earn: ${PAYE:.2f}")

    NIS = gross_salary * 2.5/100
    print(f"National Insurance Scheme: ${NIS:.2f}")

    educational_tax = gross_salary * 2.25/100
    print(f"Educational Tax: ${educational_tax:.2f}")

    total_deductions = NHT + PAYE + NIS + educational_tax
    print(f"Total Deductions: ${total_deductions:.2f}")

    Net_salary = gross_salary - total_deductions 
    print(f"Net Salary: ${Net_salary:.2f}")

    employee_count += 1
    combined_gross += gross_salary
    combined_NHT += NHT
    combined_PAYE += PAYE
    combined_NIS += NIS
    combined_education_tax += educational_tax
    combined_deductions += total_deductions
    combined_net_salary += Net_salary

    choice = input("Would you like to process another employee?")
    if choice == "yes":
        continue
    else:
        break

print(f"Total Employees: {employee_count}")
print(f"Combined Gross Salary: ${combined_gross:.2f}")
print(f"Combined NHT: ${combined_NHT:.2f}")
print(f"Combined PAYE: ${combined_PAYE:.2f}")
print(f"Combined NIS: ${combined_NIS:.2f}")
print(f"Combined Education Tax: ${combined_education_tax:.2f}")
print(f"Combined Total Deductions: ${combined_deductions:.2f}")
print(f"Combined Net Salary: ${combined_net_salary:.2f}")


















