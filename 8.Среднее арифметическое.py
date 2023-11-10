# Скласти програму, яка вводить із клавіатури чотиризначне число і виводить на екран середнє арифметичне його цифр.

# Input - 2424
# Output - 3

four_digit_number = int(input('Enter four-digit number: '))

thousands = (four_digit_number // 1000) % 10
hundreds = (four_digit_number // 100) % 10
tens = (four_digit_number // 10) % 10
units = four_digit_number % 10

average_sum = (thousands + hundreds + tens + units) / 4

print(f"Average sum of digit in {four_digit_number} = {average_sum}")