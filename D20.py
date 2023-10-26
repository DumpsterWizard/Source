import random

print("This is Dan's D20 dice simulator!")
while True:
    question = input("Roll the dice? Yes or No: \n")
    if question.lower() == "yes":
            num = random.randint(1, 20)
            print(num)
      
    else:
        print("Ok, maybe next time!")
        break
    reroll = input("Wanna roll again? \n")
    if reroll.lower() != "yes":
        print("Ok, maybe next time!")
        break

