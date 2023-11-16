value_one = 10
value_two = 16
value_three = 11

if value_one > value_two:
    print("value one is bigger than value two")
    if value_two > value_three:
        print("value two is bigger than value three")
    elif value_one > value_three:
        print("value one is bigger than value three")
    else:
        print("Some text")
else:
    print('Value three is the biggest')

print("End of code")