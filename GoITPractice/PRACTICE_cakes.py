# Булочка стоит 6 грн. 75 коп. У тебя есть n гривен. На сколько булочек тебе хватит?

CAKE = 6.75
money = int(input("How much money do you have: "))
how_many_cakes = int(money // CAKE)
print(f"You can buy {how_many_cakes}!")