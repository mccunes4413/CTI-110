#Samuel McCune
#10/31/23
#Use for loops

#Get input from user
num_1 = int(input("Enter an interger: "))
num_2 = int(input("Enter another interger: "))


if num_1 <= num_2:
    for item in range (num_1,num_2 + 1,5):
        print (item)

else:
    print("Rerun the program with the first int smaller")
