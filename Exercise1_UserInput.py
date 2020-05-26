# This program asks for user input for name and age and prints out a personalized
#message based on the user input.

userName = input("What is your name? ")
userAge = int(input("How old are you?"))
year = str((2020 - userAge) + 100)

print("Your name is: " + userName + " and you are " + str(userAge) + " years old.")

print(userName + " will be 100 years old in the year " + year + " .")

print(4 * ("Your name is: " + userName + " and you are " + str(userAge) + " years old. \n"))