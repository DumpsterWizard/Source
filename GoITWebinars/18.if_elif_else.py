# IF

value_one = 5
value_two = 10
value_three = 11

if not(value_one > value_two):
    print(value_one + value_two)

if value_three == value_two + 1:
    print("Equal")

print("End of code")

# IF ELSE

value_one = 5
value_two = 10
value_three = 11

if value_one > value_two:
    print(value_one + value_two)
else:
    print(value_one - value_three)


print("End of code")

# IF ELIF ELSE

value_one = 10
value_two = 16
value_three = 11

if value_one > value_two:
    print("value one is bigger than value two")
elif value_two > value_three:
    print("value two is bigger than value three")
elif value_one > value_three:
    print("value one is bigger than value three")
else:
    print('Value three is the biggest')

print("End of code")
