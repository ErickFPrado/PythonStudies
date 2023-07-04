# You are going to write a program that will select a random name from a list of names.
# The person selected will have to pay for everybody's food bill.

import random

names_string = input("Give me everybody's names, separated by a comma.\n")
names = names_string.split(", ")

length = len(names)

index = random.randint(0, length - 1)

print(f"{names[index]} is going to buy the meal today!")

