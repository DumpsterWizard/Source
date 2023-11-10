# Скласти програму визначення номера під'їзду та поверху квартири за заданим номером квартири. У будинку 5 поверхів і 4 квартири на поверсі.

FLOORS = 5
APARTMENTS_PER_FLOOR = 4

apartment_number = int(input("Enter apartment number: "))

apartment_per_entrance = FLOORS * APARTMENTS_PER_FLOOR
entrance_number = (apartment_number - 1) // apartment_per_entrance + 1
floor_number = ((apartment_number - 1) % apartment_per_entrance) // APARTMENTS_PER_FLOOR + 1

print(f"Entrance numbe: {entrance_number}, Floor number: {floor_number}")