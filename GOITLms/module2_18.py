# Нужно сделать функцию discount_priceна Python, которая рассчитывает конечную стоимость продукта после внедрения скидки.

# Задачи:

# Создайте функцию discount_price, которая воспринимает два аргумента: price- начальная стоимость продукта и discount- скидка как реальное число от 0до 1.
# Внутри функции discount_priceсоздавайте вложенную функцию apply_discount, которая используется nonlocalдля доступа и модификации переменной price.
# Функция apply_discountдолжна вычислить сниженную цену, умножив priceна (1 - discount).
# Вызовите apply_discountвнутри discount_priceи затем верните обновленную цену.
# Ожидаемый результат:

# Функция должна возвращать цену товара после применения скидки.

# Подсказки:

# Использование nonlocalпозволяет функции apply_discountмодифицировать переменную price, объявленную во внешней функции discount_price.
# Для расчета сниженной цены используйте формулу price * (1 - discount).



def discount_price(price, discount):
    def apply_discount():
        nonlocal price
        price = price * (1 - discount)
    apply_discount()
    return price