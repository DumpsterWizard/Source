value_one = 5
value_two = 10
value_three = 11

print("AND")
print((value_one > value_two) and (value_two > value_three))
print((value_one > value_two) and (value_two < value_three))
print((value_one < value_two) and (value_two > value_three))
print((value_one < value_two) and (value_two < value_three))

# AND -- это бинарный оператор, окруженный 2 операндами (переменными, константами или выражениями).
# Он анализирует их и выводит значение на основе следующего факта: "Он выводит значение True, только если операнды по обе стороны AND имеют значение True".

value_one = 5
value_two = 10
value_three = 11

print("OR")
print((value_one > value_two) or (value_two > value_three))
print((value_one > value_two) or (value_two < value_three))
print((value_one < value_two) or (value_two > value_three))
print((value_one < value_two) or (value_two < value_three))

# OR -- это бинарный оператор, окруженный 2 операндами (переменными, константами или выражениями). 
# Он анализирует их и выводит значение на основе следующего факта: "Он выводит значение False, только если операнды по обе стороны OR имеют значение False".

value_one = 5
value_two = 10

print(value_one > value_two)
print(not(value_one > value_two))

# NOT -- это унарный оператор, который используется для отрицания выражения после следующего оператора. 
# В соответствии с этим, каждое выражение True становится False и наоборот