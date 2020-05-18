# Exercise 1. Character Input
#
#  - Asks the user to enter their name and their age.
#  - Print out a message addressed to them that tells them the year that they will turn 100 years old.
#  - Ask the user for another number and printing out that many copies of the previous message on separate lines.

name = str(input("Hello! Please enter your name: "))
age = int(input("Thanks! Now enter your age: "))
current_year = int(input("Now please enter the current year: "))
year_turning_hundred = current_year + (100 - age)

print("\n" + name + ", you will turn a 100 years old in the year", year_turning_hundred)

multiplier = int(input("Feels good, right?\nHow many times would you like to see that again?: "))

print("\nYou're the boss! Here you go...\n")
print(("Congrats! You will be a 100 yrs. old in the year " + str(year_turning_hundred) + "\n") * multiplier)
