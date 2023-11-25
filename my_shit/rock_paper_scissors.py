import random


print("...ROCK...\n ...PAPER...\n ...SCISSORS...")



player1 = input("Rock, Paper or Scissors, player 1? (r / p / s): ")
print("NO CHEATING!!!\n NO CHEATING!!!\n NO CHEATING!!!\n NO CHEATING!!!\n NO CHEATING!!!\n NO CHEATING!!!\n NO CHEATING!!!\n NO CHEATING!!!\n NO CHEATING!!!\n NO CHEATING!!!\n NO CHEATING!!!\n NO CHEATING!!!\n NO CHEATING!!!\n NO CHEATING!!!")
player2 = input("Rock, Paper or Scissors, player 2? (r / p / s): ")

if player1 == "p" and player2 == "r":
    print("PLAYER ONE WON!")
elif player1 == "s" and player2 == "p":
    print("PLAYER ONE WON!")
elif player1 == "r" and player2 == "s":
    print("PLAYER ONE WON!")

elif player2 == "p" and player1 == "r":
    print("PLAYER TWO WON!")
elif player2 == "s" and player1 == "p":
    print("PLAYER TWO WON!")
elif player2 == "r" and player1 == "s":
    print("PLAYER TWO WON!")

elif player1 == player2:
    print("ITS A TIE! ROLL AGAIN!")

else:
    print("You must enter r or p or s!") 