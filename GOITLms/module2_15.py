# Напишите программу, которая будет выполнять простейшие математические операции с числами последовательно,
# принимая от пользователя операнды (числа) и оператор.
#
# Условия приёмки
#
# Приложение работает с целыми и дробными числами.
# Приложение умеет выполнять такие математические операции:
# СЛОЖЕНИЕ (+)
# ВЫЧИТАНИЕ (-)
# УМНОЖЕНИЕ (*)
# ДЕЛЕНИЕ (/)
# Приложение принимает один операнд или один оператор за один цикл запрос-ответ.
# Все операции приложение выполняет по мере поступления — одну за одной.
# Приложение выводит результат вычислений, когда получает от пользователя =.
# Приложение заканчивает свою работу после того, как выведет результат вычисления.
# Пользователь по очереди вводит числа и операторы.
# Если пользователь вводит оператор два раза подряд, то он получает сообщение об ошибке и может ввести повторно.
# Если пользователь вводит число два раза подряд, то он получает сообщение об ошибке и может ввести повторно.
# Приложение корректно обрабатывает ситуацию некорректного ввода (exception).
# Начальные переменные:
#
# result = None
# operand = None
# operator = None
# wait_for_number = True
# result — сюда помещаем итоговый результат operand — всегда хранит текущее число operator — строковый параметр,
# может содержать четыре значения, "+", "-", "*", "/" wait_for_number — флаг, который указывает,
# что ожидают на вводе, оператор (operator) или операнд (operand)
#
# Пример выполнения программы:
#
# >>> 3
# >>> +
# >>> 3
# >>> 2
# 2 is not '+' or '-' or '/' or '*'. Try again
# >>> -
# >>> -
# '-' is not a number. Try again.
# >>> 5
# >>> *
# >>> 3
# >>> =
# Result: 3.0
# Тестовые последовательности:
#
# Первая: ["10", "+", "5", "6", "/", "3", "-", "a", "2", "*", "6", "="], результат 18.0
# Вторая: ["2", "3", "-", "1", "+", "10", "*", "2", "="], результат 22.0

result = None
operand = None
operator = None
wait_for_number = True

while True:
    try:
        user_input = input("Enter a number: " if wait_for_number else "Enter an operator: ")

        if user_input == "=":
            if operand is not None and operator is not None:
                print("Result:", result)
            else:
                print("Invalid input. Try again.")
            break

        if wait_for_number:
            if user_input == "=":
                print("You need to enter a number first. Please try again.")
                continue
            operand = float(user_input)
            if result is None:
                result = operand
            else:
                if operator == '+':
                    result += operand
                elif operator == '-':
                    result -= operand
                elif operator == '*':
                    result *= operand
                elif operator == '/':
                    if operand == 0:
                        print("Error: Division by zero. Try again.")
                        continue
                    result /= operand

            wait_for_number = False
        else:
            if user_input in ["+", "-", "*", "/"]:
                operator = user_input
                wait_for_number = True
            else:
                print(f"{user_input} is not '+', '-', '*', or '/'. Try again.")
                continue

    except ValueError:
        print(f"{user_input} is not a number. Try again.")
    except Exception as e:
        print(f"An error occurred: {e}. Try again.")


