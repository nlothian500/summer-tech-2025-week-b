employee_count = 0
combined_gross = 0 
combined_NHT = 0
combined_PAYE = 0
combined_NIS = 0
combined_education_tax = 0
combined_deductions = 0
combined_net_salary = 0

# the while loop starts the main loop to process all the employees
while True:
    employee_id = input("Please enter the employee I.D")
# employee_id asks the user to enter the employee ID 
    employee_name = input("Please enter the employee full name: ")
# employee_name asks the user to enter the name of the employee
    while True: # This while loop is created because if the user enters a invalid employment_status the loop will run until a valid one is entered
        employment_status = input("Please enter the employee status: ")
        #employment_status asks the user to enter the employee status monthly or fortnightly
        if employment_status == "fortnightly":
            hourly_rate = 550
            break # the if statement says that if employment_status is == to fortnightly then assign the hourly rate to $550
        elif employment_status == "monthly": # this elif statement checks if the employee is monthly
            hourly_rate = 1200 # This line is assigns $1200 if the user enters monthly
            break
        else: # this else statement is saying that if an invalid employment status is entered. The code would say Invalid employment status try again
            print("Invalid employment status try again")
            continue
                
    hours_work = int(input("Please enter the number of hours the employee worked: "))
    #this asks the user to enter the number of hours the employee worked
    # the while loop repeats if the number of hours is negative
    while hours_work < 0:
        print("Invalid hours the hours cannot be negative")
        hours_work = int(input("Please enter the number of hours the employee worked: "))

    gross_salary = hourly_rate * hours_work
    print(f"Gross Salary: ${gross_salary:.2f}")
    # line 36 calculates the gross salary and line 37 displays the gross salary

    NHT = gross_salary * 2/100
    print(f"National Housing Trust: ${NHT:.2f}")
    # Line 40 Calculates the the NHT and line 41 displays it

    PAYE = gross_salary * 25/100
    print(f"Pay As You Earn: ${PAYE:.2f}")
    # Line 44 calculates the PAYE and line 45 displays it

    NIS = gross_salary * 2.5/100
    print(f"National Insurance Scheme: ${NIS:.2f}")
    #line 48 calculates the NIS and Line 49 displays it

    educational_tax = gross_salary * 2.25/100
    print(f"Educational Tax: ${educational_tax:.2f}")
    # Line 52 calculates the Educational tax and line 53 displays it

    total_deductions = NHT + PAYE + NIS + educational_tax
    print(f"Total Deductions: ${total_deductions:.2f}")
    #line 56 calcualtes the sum of NIS,PAYE,NHT and Educational tax and line 57 displays it 

    Net_salary = gross_salary - total_deductions 
    print(f"Net Salary: ${Net_salary:.2f}")
    #line 60 subtracts the gross salary from the total deductions and line 61 displays it

    employee_count += 1
    combined_gross += gross_salary
    combined_NHT += NHT
    combined_PAYE += PAYE
    combined_NIS += NIS
    combined_education_tax += educational_tax
    combined_deductions += total_deductions
    combined_net_salary += Net_salary

    choice = input("Would you like to process another employee?") # this asks if the useer wants to process and employee 
    if choice == "yes": # this checks if the user wants to process another employee 
        continue # Returns to the beginning of the main loop
    else:
        break # if the user does not enter yes, stop the main loop 

print("Payroll Summary: ")
print(f"Total Employees: {employee_count}")
print(f"Combined Gross Salary: ${combined_gross:.2f}")
print(f"Combined NHT: ${combined_NHT:.2f}")
print(f"Combined PAYE: ${combined_PAYE:.2f}")
print(f"Combined NIS: ${combined_NIS:.2f}")
print(f"Combined Education Tax: ${combined_education_tax:.2f}")
print(f"Combined Total Deductions: ${combined_deductions:.2f}")
print(f"Combined Net Salary: ${combined_net_salary:.2f}")

