# You are going to write a virtual coin toss program. It will randomly tell the user "Heads" or "Tails".

import random

result = random.randint(0, 1)

if result == 0:
    print("Tails")
else:
    print("Heads")
