#Samuel McCune
#11/9/23
#Uses if/else Statements

num_employees = 0
total_paid_out = 0

#Get employee name from user
name = input("Enter Your Employee Name: ")

while name != "Done":
    num_employees += 1
    #Get number of hours from user
    Hours = int(input("Number of hours: "))
    #Get payrate per hour from user
    Payrate = float(input("Enter your Payrate: "))
    #Determine if employee worked more than 40 hours
    #Calculate OT hours
    if Hours> 40:
        OT = Hours - 40
    else:
        OT = 0
    #Calculate reg hours worked
    if Hours<= 40:
        RegHours = Hours
    else:
        RegHours = 40
    #Calculate pay for reg hours
    regpay = RegHours * Payrate


    #Calculate OT pay
    overtimepay = OT * (Payrate * 1.5)
    gross_pay = regpay + overtimepay
    total_paid_out += gross_pay
    name = input("Enter Your Employee Name: ")



#Display name, payrate, reg hours, OT hours, OT pay, gross pay

print("------------------------")
print(num_employees, "have been added.")
print("The total paid out to all employees is", total_paid_out)
