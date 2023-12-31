# В Харькове открывают бомбоубежище в школе для молодых учеников.
# Нужно обеспечить три комнаты партами. Одна парта на два ученика.
# Программе подается на вход 3 числа, (тремя input) - колличество учеников в классе.
# Программа должна подсчитать необходимое кол-во парт в общем.

class_a = int(input("How many students in class A: "))
class_b = int(input("How many students in class B: "))
class_c = int(input("How many students in class C: "))

desks_a = class_a // 2     #вычисляется количество парт в каждом классе. Поскольку в задании указано,  
desks_b = class_b // 2     #что на одну парту приходится два ученика,
desks_c = class_c // 2     #используется оператор целочисленного деления // для разделения общего числа учеников на два.

a_add = class_a % 2        #Далее, для каждого класса, проверяется, есть ли у нас остаток от деления, который 
b_add = class_b % 2        #может быть равен 1 (если количество учеников нечетное). Если есть остаток, 
c_add = class_c % 2        #добавляется одна дополнительная партa.

print(desks_a + desks_b + desks_c + a_add + b_add + c_add)  #И, наконец, выводится общее количество парт, учитывая основные парты и дополнительные.

#Таким образом, программа принимает ввод по количеству учеников в трех классах, 
#вычисляет необходимое количество парт и выводит общее число парт, учитывая возможные дополнительные парты из-за нечетного числа учеников.