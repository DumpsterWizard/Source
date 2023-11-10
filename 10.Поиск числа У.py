# # У тризначному числі х закреслили його другу цифру.
#  Коли до двозначного числа, що утворилося, ліворуч приписали другу цифру числа х, то вийшло число y. 
# Скласти програму знаходження числа y.
# Input - 971
# Otput - 791

three_digit_number = int(input('Enter three-digit number: '))

hundreds = (three_digit_number // 100) % 10
tens = (three_digit_number // 10) % 10
units = three_digit_number % 10

result_number = tens * 100 + hundreds * 10 + units
# result_number = str(tens)+str(hundreds)+str(units)

print(f"Result = {result_number}")