#Samuel McCune
#10/26/23
#Uses if/else Statements

#Get employee name from user
employeename = input("Enter Your Employee Name: ")
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
#Display name, payrate, reg hours, OT hours, OT pay, gross pay
print("Name: ",employeename)
print("Pay Rate:",Payrate)
print("Regular pay: ",regpay)
print("Overtime Hours: ",OT)
print("Overtime pay: ",overtimepay)
print("Gross pay: ",regpay + overtimepay)
