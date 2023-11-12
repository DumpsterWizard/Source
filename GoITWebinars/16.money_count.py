# Для кава-брейків на конференції закуплено: х круасанів, у стаканчиків, z упаковок кави. 
# Ціна круасана $1.04, ціна стаканчика - $0.34, ціна упаковки кави $4.42. 
# Скласти програму, яка обчислює, скільки повних доларів пішло на закупівлю їжі для кава-брейків, і яка її вартість у доларах і центах.

# Input_croissants - 4
# Input_cups - 5
# Input_coffee - 6
# Output_dollars - 32
# Output_cents - 3238

PRICE_CROISSANTS = 1.04
PRICE_CUPS = 0.34
PRICE_COFFEE = 4.42

croissants = int(input("Enter croissants: "))
cups = int(input("Enter cups: "))
coffee = int(input("Enter coffee: "))

sum_dollars = croissants * PRICE_CROISSANTS + \
              cups * PRICE_CUPS + \
              coffee * PRICE_COFFEE

only_dollars = int(sum_dollars)
sum_cents = int(sum_dollars*100)

print(f"Dollars = {only_dollars}, Cents = {sum_cents}")