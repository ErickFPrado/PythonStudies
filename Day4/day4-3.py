# You are going to write a program that will mark a spot with an X.

row1 = ["⬜️", "️⬜️", "️⬜️"]
row2 = ["⬜️", "⬜️", "️⬜️"]
row3 = ["⬜️️", "⬜️️", "⬜️️"]

mapa = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}")
position = (input("Where do you want to put the treasure? "))

index1 = int((position[0])) - 1
index2 = int((position[1])) - 1

mapa[index2][index1] = "X"

print(mapa)
