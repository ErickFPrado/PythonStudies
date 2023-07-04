# You are going to write a program that tests the compatibility between two people.
#
# To work out the love score between two people:
#
# Take both people's names and check for the number of times the letters in the word TRUE occurs.
#
# Then check for the number of times the letters in the word LOVE occurs.
#
# Then combine these numbers to make a 2-digit number.

print("Welcome to the Love Calculator!")
name1 = (input("What is your name? \n"))
name2 = (input("What is their name? \n"))

# Lowercase the string
name1 = name1.lower()
name2 = name2.lower()

# Put thing together
verify = name1 + name2

# Verifying TRUE LOVE
true = 0
love = 0

true += verify.count("t")
true += verify.count("r")
true += verify.count("u")
true += verify.count("e")

love += verify.count("l")
love += verify.count("o")
love += verify.count("v")
love += verify.count("e")


total = int(str(true) + str(love))


if total < 10 or total > 90:
    print(f"Your score is {total}, you go together like coke and mentos")
elif 40 < total < 50:
    print(f"Your score is {total}, you are alright together")
else:
    print(f"Your score is {total}")

