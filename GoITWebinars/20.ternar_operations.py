value_x, value_y = 5, 7

max_value = value_x if value_x > value_y else value_y
print(max_value)
max_value = "X > Y" if value_x > value_y else "X < Y"
print(max_value)


if value_x > value_y:
    print("X > Y")
else:
    print("X < Y")

# [statement_1] if [expression] else [statement_2]
# Использование тернарного оператора для определения четности или нечетности числа