#Samuel McCune
#10/5/23
#Dictionaries

name = input("Enter your name: ")
hair = input("Enter your hair color: ")
eye = input("Enter your eye color: ")
height = float(input("Enter height as a decimal: "))
age = input("Enter your age: ")
food = input("Whats your favorite food?: ")

#Create a Dictionary
my_dict = {"Name": name, "Hair_Color": hair, "Eye_Color": eye, "Height": height, "Age": age, "Favorite_Food": food,}

#Get valuees using the key
print(f"{my_dict['Name']} is a {my_dict['Height']} tall student with {my_dict['Hair_Color']} hair and {my_dict['Eye_Color']} eyes. They are {my_dict['Age']} years old and their favorite food is {my_dict['Favorite_Food']}.")
