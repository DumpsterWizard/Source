from random import randint

print("...ROCK...\n ...PAPER...\n ...SCISSORS...")



# player1 = input("Rock, Paper or Scissors, player 1? (r / p / s): ")
# print("NO CHEATING!!!\n" *20)

# player2 = input("Rock, Paper or Scissors, player 2? (r / p / s): ")

# if player1 == "p" and player2 == "r":
#     print("PLAYER ONE WON!")
# elif player1 == "s" and player2 == "p":
#     print("PLAYER ONE WON!")
# elif player1 == "r" and player2 == "s":
#     print("PLAYER ONE WON!")

# elif player2 == "p" and player1 == "r":
#     print("PLAYER TWO WON!")
# elif player2 == "s" and player1 == "p":
#     print("PLAYER TWO WON!")
# elif player2 == "r" and player1 == "s":
#     print("PLAYER TWO WON!")


# if player1 == "p":
#     if player2 == "r":
#         print("Player one wins!")
# if player1 == "s":
#     if player2 == "p":
#         print("Player one wins!")
# if player1 == "r":
#     if player2 == "s":
#         print("Player one wins!")

# if player2 == "p":
#     if player1 == "r":
#         print("Player two wins!")
# if player2 == "s":
#     if player1 == "p":
#         print("Player two wins!")
# if player2 == "r":
#     if player1 == "s":
#         print("Player two wins!")

# if player1 == player2:
#     print("ITS A TIE! ROLL AGAIN!")

# elif player1 == "p":
#     if player2 == "r":
#         print("Player one wins!")
#     elif player2 == "s":
#         print("Player two wins!")
# if player1 == "s":
#     if player2 == "r":
#         print("Player two wins!")
#     elif player2 == "p":
#         print("Player one wins!")
# if player1 == "r":
#     if player2 == "s":
#         print("Player one wins!")
#     elif player2 == "p":
#         print("Player two wins!")

# else:
#     print("You must enter r or p or s!") 


player = input("Enter rock, paper or scissors (r / p / s): ")


random_move = randint(0, 2)
if random_move == 0:
    computer = "r"
elif random_move == 1:
    computer = "s"
else:
    computer = "p"

if player == computer:
    print("ITS A TIE! ROLL AGAIN!")

if player == "r":
    if computer == "s":
        print("Player wins!")
    elif computer == "p":
        print("Computer wins!")
if player == "s":
    if computer == "r":
        print("Computer wins!")
    elif computer == "p":
        print("Player wins!")
if player == "p":
    if computer == "s":
        print("Computer wins!")
    elif computer == "r":
        print("Player wins!")
else:
        print("Enter valid item!")