# Скласти програму обчислення площі та гіпотенузи прямокутного трикутника, якщо відомі його катети (вводяться користувачем)

cathet1 = float(input("Enter cathet 1 please: "))
cathet2 = float(input("Enter cathet 2 please: "))
s_area = 2 * (cathet1 * cathet2)
hypothenuza = (cathet1**2 + cathet2**2)**0.5 
print(f"Если первый катет равен {cathet1}, а второй равен {cathet2}, то площадь прямоугольного треугольника равна {s_area}, а его гипотенуза {hypothenuza}")


# first_cathetus = float(input('Enter first cathetus: '))
# second_cathetus = float(input('Enter second cathetus: '))

# area = (first_cathetus * second_cathetus) / 2
# hypotenuse = (first_cathetus ** 2 + second_cathetus ** 2) ** 0.5

# print(f'Hypotenuse = {hypotenuse}; Area = {area}')