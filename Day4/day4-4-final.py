# rock, paper or scissors program
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print("Welcome to the Rock, Paper or Scissors Program")
user_input = input("Choose between rock, paper or scissors:\n").lower()

value = 0
output = 0

if user_input == "rock":
    value = 0
    output = rock

elif user_input == "paper":
    value = 1
    output = paper
elif user_input == "scissors":
    value = 2
    output = scissors
else:
    print("Invalid input! Choose between Rock, Paper or Scissors")
    exit()

computer_choose = random.randint(0, 2)
output_computer = 0
name_computer = 0

if computer_choose == 0:
    output_computer = rock
    name_computer = "rock"
elif computer_choose == 1:
    output_computer = paper
    name_computer = "paper"
else:
    output_computer = scissors
    name_computer = "scissors"

print(f"You choose {user_input} \n {output}")
print(f"Computer choose {name_computer} \n {output_computer}")

if value == computer_choose:
    print(f"That's a draw!")
else:
    if (value == 0 and computer_choose == 2) or (value == 1 and computer_choose == 0) or (value == 2 and
                                                                                          computer_choose == 1):
        print(f"You win!!")
    else:
        print(f"You lose!")
