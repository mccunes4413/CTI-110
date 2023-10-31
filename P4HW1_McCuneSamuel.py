#Samuel McCune
#10/10/23
#Working with lists

#Create varibles and get user input (6)
num_grades = int(input("How many grades will you enter? "))
#create empty list
grade_list = []

for grade in range(num_grades):
    this_grade = int(input("enter a grade: "))
    while this_grade < 0 or this_grade > 100:
        print("Invalid grade entered.")
        this_grade = int(input("Enter a grade"))
        
    grade_list.append(this_grade)
    print(f"{this_grade} has been added to the list")


for grade in grade_list:
    print(grade)



print()
#Calculate min/max/sum/average and assign to varibles
max_value = max(grade_list)
min_value = min(grade_list)
grade_list.remove(min_value)
sum_value = sum(grade_list)
length_value = len(grade_list)
#Display info to user use print () statements
print("Max: ", max_value)
print("Min: ", min(grade_list))
print("Sum: ", sum(grade_list))
print("Average: ", sum_value/length_value)
