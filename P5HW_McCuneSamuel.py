#Samuel McCune
#11/16/23
#Using if/else, loop, functions and random numbers

import random

def show_menu():
    print()
    print("Welcome to the Math Quiz")
    print("MAIN MENU")
    print("-------------------")
    print("1. Adding Random Numbers")
    print("2. Subtracting Random Numbers")
    print("3. Exit Program")

def adding():
    random_1 = random.randint(0,10)
    random_2 = random.randint(0,10)
    my_sum = random_1 + random_2
    print(f"      {random_1}")
    print("+")
    print(f"      {random_2}")
    return my_sum

def subtracting():
    random_1 = random.randint(0,10)
    random_2 = random.randint(0,10)
    my_diff = random_1 - random_2
    print(f"      {random_1}")
    print("-")
    print(f"      {random_2}")
    return my_diff

def guessing(guess, value):
    num_guess = 0
    while guess != value:
        num_guess += 1

        if guess > value:
               print("Your guess is too high")
               guess = int(input("Enter your guess: "))
        else:
                print("Your guess is too low")
                guess = int(input("Enter your guess: "))
    print("Congrats, your guess was correct")
    print(f"It took you {num_guess} guesses")


#Main function that runs the program
def main():
    while True:
        show_menu()
        user_choice = int(input("Please choose one of the menu options: "))
        if user_choice == 1:
            value = adding()
            guess = int(input("Enter your guess: "))
            guessing(guess, value)
            
        if user_choice == 2:
            value = subtracting()
            guess = int(input("Enter your guess: "))
            guessing(guess, value)
             
        if user_choice == 3:
            print("The Program has Ended")
            break

#Call the main function
if __name__ == "__main__":
    main()
