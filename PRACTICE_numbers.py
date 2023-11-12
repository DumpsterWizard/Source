# Считайте действительное число, Введите его первую цифру после точки.
# 123.456

a = float(input("Enter real number: "))
b = int(a)
c = a - b  # 0.456
c = int(c * 10)  # 4.56
print(c)