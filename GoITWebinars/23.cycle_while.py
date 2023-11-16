start = 1

while start <= 5:
    print(start)
    start += 1

# Как можно динамически прервать цикл с помощью If условия

condition = True
start = 1

while condition:
    if start == 7:
        condition = False
    print(start)
    start += 1

print('Out of the loop')

# Сколько чисел необходимо, чтобы сумма вида 1+2+3+4+... стала больше 100

sum = 0
counter = 1
condition = True

while True:
    sum += counter
    if sum > 100:
        break
    counter += 1

print(f"Sum {sum} last value is {counter}")

# While и For может использоваться с else значением

word = 'python'

for char in word:
    if char == 'o':
        print('There is O in word')
        break
else:
    print('There is no O in word')

# _____________________________________________
increment = 0

while increment <= 3:
    print(increment, end=' ')
    increment += 1
else:
    print(0)