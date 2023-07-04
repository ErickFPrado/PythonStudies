# Program that calculates the sum of all the even numbers from 1 to 100.

sum_of_numbers = 0
for even in range(2, 101, 2):
    sum_of_numbers += even

print(sum_of_numbers)
