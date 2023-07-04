# Program that calculates the average student height from a List of heights.

student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

total_height = 0
for height in student_heights:
    total_height += height

num_students = 0
for student in student_heights:
    num_students += 1

print(round(total_height/num_students))



