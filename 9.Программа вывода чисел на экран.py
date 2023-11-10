# Скласти програму, яка вводить з клавіатури тризначне число і виводить на екран

# суму останньої та передостанньої цифри
# суму останньої та першої цифри.

three_digit_number = int(input('Enter three-digit number: '))

hundreds = (three_digit_number // 100) % 10
tens = (three_digit_number // 10) % 10
units = three_digit_number % 10

sum_tens_units = tens + units
sum_hundreds_units = hundreds + units

print(f"The sum of the last and penultimate digit is {sum_tens_units}")
print(f"The sum of the last and first digit is {sum_hundreds_units}")