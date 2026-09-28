from random import randint
termchoice = randint(1,3) #1 is rock 2 is paper and 3 is scissors
print("welcome to Rock, Paper, Scissors!")
print("Enter your choice: 1 for Rock, 2 for Paper, 3 for Scissors!")
yourchoice = int(input())

if yourchoice == termchoice:
    print("Its a tie")
elif (yourchoice == 1 and termchoice == 3) or (yourchoice == 3 and termchoice == 1):
    print("you win")
elif (yourchoice == 1 and termchoice == 2) or (yourchoice == 3 and termchoice == 2):
    print("term wins")
elif yourchoice < 1 or yourchoice > 3:
    print("Invalid choice. Please enter 1, 2 or 3.")
elif termchoice < 1 or termchoice > 3:
    print("Invalid choice. Please enter 1, 2 or 3.")
elif yourchoice == 1:
    print("you chose rock")
elif yourchoice == 2:
    print("you chose Paper")
elif yourchoice == 3:
    print("you chose Scissors")





