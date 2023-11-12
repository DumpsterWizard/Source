#С начала суток прошло n минут. Программа принимает это число input-ом.
#Какое время будет показывать электронное табло часов?
#Программа должна вывести два числа - часы(от 0 - 23), и минуты (от 0 - 59).

n = int(input("How many times past: "))
full_h = (n // 60) % 24
# Эта строка вычисляет количество полных часов, прошедших с начала суток. 
# n // 60 дает количество часов, а % 24 обеспечивает цикличность в 24 часах (если n больше 1440, то остаток от деления на 24 часа).
minute = n % 60 # Эта строка вычисляет количество минут, оставшихся после выделения полных часов.
print(n, full_h, minute)
