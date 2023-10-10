#Samuel McCune
#10/10/23
#Working with lists

#Create varibles and get user input (6)

module1 = int(input("Enter Grade 1: "))
module2 = int(input("Enter Grade 2: "))
module3 = int(input("Enter Grade 3: "))
module4 = int(input("Enter Grade 4: "))
module5 = int(input("Enter Grade 5: "))
module6 = int(input("Enter Grade 6: "))
#Add to a list
next_list=[module1, module2, module3, module4, module5, module6]

print(next_list)
#Create an empty list


print()
#Calculate min/max/sum/average and assign to varibles
max_value = max(next_list)
min_value = min(next_list)
sum_value = sum(next_list)
length_value = len(next_list)
#Display info to user use print () statements
print("Max: ", max_value)
print("Min: ", min(next_list))
print("Sum: ", sum(next_list))
print("Average: ", sum_value/length_value)
