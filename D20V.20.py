import random

print("This is Dan's D20 dice simulator!")

first_roll = True  # Устанавливаем флаг первого броска

while True:
    if first_roll:
        question = input("Roll the dice? Yes or No: ").strip().lower()
        first_roll = False  # После первой итерации снимаем флаг
    else:
        question = input("Wanna roll again? ").strip().lower()

    if question == "yes":
        num = random.randint(1, 20)
        print(num)
    elif question == "no":
        print("Ok, maybe next time!")
        break
    else:
        print("Please enter 'yes' or 'no'.")

# сравнить с первой версией