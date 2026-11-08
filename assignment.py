while True:
    employee_id = input("Please enter the employee I.D")

    employee_name = input("Please enter the employee full name: ")

    employment_status = input("Please enter the employee status: ")
    if employment_status == "fortnightly":
        hourly_rate = 550
    elif employment_status == "monthly":
        hourly_rate = 1200
    else:
        print("Invalid employment status try again")
        

    hours_work = int(input("Please enter the number of hours the employee worked: "))
    if hours_work < 0:
        print("Invalid hours the hours cannot be negative")
        break

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


    choice = input("Would you like to process another employee?")
    if choice == "yes":
        continue
    else:
        break

















