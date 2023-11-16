# Найти сумму чисел в определенном диапазоне
sum = 0
maximum = 11

for element in range(1, maximum+1):
    print(sum, element)
    sum += element

print(sum)


# Программа читает число n количества входных значений, а далее читает n значений. И считает сумму и среднее арифметическое этих значений.

number_count = int(input("Enter range of number: "))
sum = 0

for _ in range(0, number_count):
    number = int(input("Enter value: "))
    sum = sum + number

# Variant 2
# for i in range(1, number_count+1):
#     number = int(input(f"Enter value of element {i}: "))
#     sum = sum + number

print(f"Sum equal {sum} and average value equal {round(sum/number_count,2)}")