# Ситуация простая, вам необходимо высчитать количество SMS, которые надо отправлять в одном пакете рассылки потенциальным покупателям.
# Всего в день выделяется 1000 платных SMS для кампании маркетинга pool = 1000.
# Сотрудник отдела маркетинга вводит количество рассылок quantity и вы высчитываете размер пакет chunk = pool // quantity.
# Обработайте ошибку деления на ноль.

pool = 1000

try:
    quantity = int(input("Enter the number of mailings: "))
    chunk = pool // quantity
    print(f"Size of each mailing chunk: {chunk}")
except ZeroDivisionError:
    print('Error: Division by zero is not allowed!')