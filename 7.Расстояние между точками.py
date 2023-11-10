# Скласти програму обчислення відстані між точками з координатами, що вводяться користувачем.

x1_coord = float(input("Enter x1 coordinate: "))
y1_coord = float(input("Enter y1 coordinate: "))
x2_coord = float(input("Enter x2 coordinate: "))
y2_coord = float(input("Enter y2 coordinate: "))

distance = round(((x1_coord - x2_coord)**2 + (y1_coord - y2_coord)**2)**0.5, 2)

print("Distance = ", distance)

# Distance - sqrt((x2-x1)^2 + (y2-y1)^2)

# from math import sqrt, pow

# x1_coord = float(input("Enter the x coord of the first point "))
# y1_coord = float(input("Enter the y coord of the first point "))

# x2_coord = float(input("Enter the x coord of the second point "))
# y2_coord = float(input("Enter the y coord of the second point "))

# distance = round(((x2_coord - x1_coord)**2 + (y2_coord - y1_coord)**2) ** 0.5, 2)

# print('Distance = ', distance)

# # Second variant
# print("sqrt((x2-x1)^2 + (y2-y1)^2) = ",
#       round(sqrt(pow(x2_coord-x1_coord, 2) + pow(y2_coord-y1_coord, 2)), 2))