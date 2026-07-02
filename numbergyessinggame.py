import random

number=random.randint(1,100)
guess=0
attempts=0
print("~~Welcome to the number guessing game~~")
print("GUESS THE NUMBER 1-100")
while guess!=number:
    guess=int(input("enter the number you guess:"))
    attempts+=1
    if guess>number:
        print("TOO HIGH TO GUESS,TRY AGAIN")
    elif guess<number:
        print("TOO LOW TO WIN ,TRY AGAIN")
    else:
        print("~~CONGRATS YOU WON~~")
    print("the total number of attempts:",attempts)
