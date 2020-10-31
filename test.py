#!/usr/bin/python3
import random
user = 0
time = -1
"""
-1:random
1(computer last win):(computer --)
0(cpmouter last lost or draw):(computer ++)
from <<Socialcycling and conditional responses in the Rock-Paper-Scissors Game>>
"""
while True:
    try:
        user_raw = input("Please input: scissors(0), rock(1), paper(2) or Quit(3):")
        user = int(user_raw)
        if user == 3:
            break
        if time ==-1:
            computer = random.randint(0,2)
        elif time ==1:
            computer = (computer-1+3)%3
        else :
            computer = (computer+1)%3
        print("You:",user," Computer:",computer)
        if(user == 0 and computer == 2) or (user == 1 and computer == 0) or (user == 2 and computer ==1):
            print("You Win!")
        elif computer==user:
            print("Draw!")
        else:
            print("You Lost.")
    except(ValueError):
        print("Please input a number.")
