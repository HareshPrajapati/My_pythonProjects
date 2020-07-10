import random


x=random.randint(0,100)
i=0
print("Guess the number")
while(i<=9):
    a=int(input())
    if a<x:
        print("You entered a smaller number")
        i=i+1
    elif a>x:
        print("You entered a larger number")
        i=i+1
    else:
        print("you won")
        print("you take",i,"guesses to finish the game")
        break

if i==10:
    print("you loss")