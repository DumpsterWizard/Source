# Перепишите пример из теории, но для положительного числа проверяйте — четное оно или нет. 
# Таким образом после проверок переменная result должна содержать одно из четырех значений:

# "Positive even number"
# "Positive odd number"
# "Negative number"
# "It is zero"
# Подсказка: проверка на четность выполняется сравнением остатка от деления на 2 с 0 или 1. Напомним, остаток от деления можно получить после операции %

num = int(input("Enter a number: "))

if num > 0:
    if num % 2:
        result = "Positive odd number"
    else:
        result = "Positive even number"
elif num < 0:
    result = "Negative number"
else:
    result = "It is zero"
print(result)