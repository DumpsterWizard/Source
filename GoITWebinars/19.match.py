value_x = -4

match value_x:
    case 0: print('value is zero')
    case 4 if value_x % 2 == 0:
        print('x % 2 == 0 and case is 4')
    case _ if value_x < 0:
        print('Value is negative')
    case _:
        print(value_x)

# Оператор match принимает значение, которое поступает на вход и с помощью case заменяет if...elif...else