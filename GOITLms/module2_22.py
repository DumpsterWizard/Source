# Мы проводим розыгрыш призов среди первых 50 подписчиков ютуб-канала. У нас есть 7 призов для розыгрыша. Может возникнуть вопрос, сколько разных списков победителей мы можем получить во время розыгрыша? Для этого мы будем использовать формулу сочетаний без повторений

# Cnk = n ! /((n – k)! · k!)

# где n– это общее количество людей (случаев), а k– количество людей, получивших призы.

# Напишите функцию number_of_groups, которая принимает параметры nи k, и с помощью функции factorialвозвращает нам сколько разных списков победителей мы можем получить при розыгрыше

# Задачи:

# Создайте функцию number_of_groups, которая принимает два аргумента: nобщее количество людей и kколичество победителей.
# В функции number_of_groupsиспользуйте функцию factorialдля вычисления факториалов в соответствии с формулой сочетаний: C n k = n! /((n – k)! · k!).
# Вычисление осуществляется путем вызова функции для factorialполучения факториалов nи n - k.k
# Возвратите результат этого вычисления.
# Ожидаемый результат:

# Функция number_of_groupsвозвращает количество возможных списков победителей.

# Обратите внимание, какие большие значения мы получаем для факториала. Рекурсивные высказывания следует всегда применять с осторожностью при вычислениях, чтобы не получить переполнение памяти.


def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n - 1)

def number_of_groups(n, k):
    numerator = factorial(n)
    denominator = factorial(n - k) * factorial(k)
    return numerator // denominator