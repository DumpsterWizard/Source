# Напишите функцию get_fullnameна Python, которая принимает имя, фамилию и, опционально, второе имя (или отчество) и возвращает строку с полным именем пользователя.

# Задачи:

# Создайте функцию get_fullname, которая принимает три аргумента: first_name, last_nameи middle_name. Сделайте middle_nameнеобязательным аргументом со значением по умолчанию "".
# Если middle_nameпередано, то функция должна возвращать полное имя в формате 'first_name middle_name last_name'.
# Если middle_nameне передано, функция должна возвращать полное имя в формате 'first_name last_name'.
# Для формирования полного имени используйте f-строку.
# Ожидаемый результат:

# Функция возвращает строку с полным именем пользователя, в зависимости от того, передано ли второе имя.

# Подсказки:

# Используйте условную конструкцию ifдля проверки, не пусто ли middle_name.
# Для создания строки с полным именем используйте f-строку для вставки значений переменных.


def get_fullname(first_name, last_name, middle_name=""):
    if middle_name:
        return f"{first_name} {middle_name} {last_name}"
    else:
        return f"{first_name} {last_name}"