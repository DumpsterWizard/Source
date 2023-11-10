# В Інтернет-магазині зроблено 4 покупки: на $34.34, $12.01, $17.42, $4.93. Зі скількох доларів і центів складатиметься підсумкова сума.

# Input - 34.34, 12.01, 17.42, 4.93
# Output_dollars - 68
# Outputs_cents - 70

bill_one = 34.34
bill_two = 12.01
bill_three = 17.42
bill_four = 4.93

total = bill_one + bill_two + bill_three + bill_four

dollars = int(total)
cents = int((total - dollars) * 100)
# cents = round((total - dollars) * 100) # вирішує проблему з округленням

print(f"Price = {total}", f"Dollars = {dollars}", f"Cents = {cents}", sep='\n')