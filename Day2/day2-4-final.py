# If the bill was $150.00, split between 5 people, with 12% tip.

# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60

# Bill calculator

print("Welcome to eh tip calculator!")

total_bill = float(input("What was the total bill? \n$ "))
tip = int(input("How much tip would you like to give? 10, 12, or 15? \n"))
people = int(input("How may people to split the bill? \n"))

account = (total_bill * tip / 100) + total_bill
result = account / people

print(f"Each person should pay: ${round(result, 2)}")
