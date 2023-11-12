# С Польши гоним машину. За день машина проезжает m км.
# На какой день машина доедет до нового хозяина, если нужно проехать n км?
import math
m = int(input("Enter how many km's goes car in 1 day: "))
n = int(input("Enter km's to home: "))

days = n / m 
print(math.ceil(days))   #Сводка Метод Math. ceil() - округление вверх. Округляет аргумент до ближайшего большего целого.