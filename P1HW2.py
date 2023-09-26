#Samuel McCune
#9/26/23
#Calculates travel expences

budget = int(input("Enter Budget: "))

dest = input("Where are you traveling? ")

gas = int(input("Enter gas Budget: "))
food = int(input("Enter food Budget: "))
hotel = int(input("Enter hotel Budget: "))

expenses = gas+food+hotel

print("--------Travel Expenses-----------")
print("Location: ", dest)
print("Initial Budget:", budget)
print()
print("Gas Cost: ", gas)
print("Food Cost: ", food)
print("Hotel Cost: ", hotel)
print()
print("Remaining Balance: ", budget-expenses)
