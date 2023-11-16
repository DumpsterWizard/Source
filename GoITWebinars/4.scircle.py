# Дано радіус кола r (вводяться користувачем). Скласти програму знаходження довжини кола та площі кола
# C = 2 π ⋅ R

PI = 3.14

radius = float(input("Enter radius: "))

length = 2 * PI * radius
s_area = PI * radius**2
print(f"Площадь вашего круга составляет {round(s_area), 2}, а длина {round(length), 2}")

# from math import pi as PI
# PI = 3.14
# 20
# radius = float(input("Enter circle radius: "))

# circle_lenght = 2 * PI * radius
# circle_area = PI * radius ** 2

# print(f"Radius circle = {radius}\
#       Lenght of circle = {round(circle_lenght, 2)}\
#       Area = {round(circle_area, 2)}")