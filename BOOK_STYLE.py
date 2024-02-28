# # Программа подсчета слов!
# line = input("Enter your text here, please!: ")
# counted_line = line.count(" ") + 1
# print(counted_line)




# PI = 3.141592653589793
# radius = int(input())
# height = int(input())
# volume = (PI * radius**2 * height) / 3
# print(volume)




# number = int(input())
# print("sp" + ("o" * number) + "ky")




# far = int(input()) * "far, "
# print("A long time ago in a galaxy " + far.rstrip(", ") + " away...")




# Y = int(input())
# M = int(input())
# print(M + (M - Y))




# c = int(input())
# print((c * 9 / 5) + 32)




# paint = int(input())
# paint_per_badge = int(input())
# price_per_badge = int(input())

# num_badges = paint // paint_per_badge  #calculate number of badges we can make
# money_from_badges = num_badges * price_per_badge # Calculate money from selling badges
# remaining_paint = paint % paint_per_badge # calculate remaining paint
# money_from_rem_paint = remaining_paint # calculate money  from selling rem paint
# total_money = money_from_badges + money_from_rem_paint # calculate total money we will make
# print(total_money)




# a3 = int(input())
# a2 = int(input())
# a1 = int(input())
# a_total = (a3 * 3) + (a2 * 2) + a1

# b3 = int(input())
# b2 = int(input())
# b1 = int(input())
# b_total = (b3 * 3) + (b2 * 2) + b1

# if a_total > b_total:
#     print("A")
# elif a_total < b_total:
#     print("B")
# else:
#     print("T")




# num1 = int(input())
# num2 = int(input())
# num3 = int(input())
# num4 = int(input())

# if ((num1 == 8 or num1 == 9) and (num4 == 8 or num4 == 9) and (num2 == num3)):
#     print("ignore")
# else:
#     print("answer")



# burger = int(input())
# side = int(input())
# drink = int(input())
# dessert = int(input())

# if burger == 1:
#     burger = 461
# elif burger == 2:
#     burger = 431
# elif burger == 3:
#     burger = 420
# else:
#     burger = 0

# if drink == 1:
#     drink = 130
# elif drink == 2:
#     drink = 160
# elif drink == 3:
#     drink = 118
# else:
#     drink = 0

# if side == 1:
#     side = 100
# elif side == 2:
#     side = 57
# elif side == 3:
#     side = 70
# else: 
#     side = 0

# if dessert == 1:
#     dessert = 167
# elif dessert == 2:
#     dessert = 266
# elif dessert == 3:
#     dessert = 75
# else:
#     dessert = 0

# total = burger + side + drink + dessert

# print("Your total Calorie count is " + str(total) + ".")



# month = int(input())
# day = int(input())

# if month < 2 and day < 18 or month < 2 and day > 18:
#     print("Before")
# elif month > 2 and day > 18 or month > 2 and day < 18:
#     print("After")
# else:
#     print("Special")

# И ОТ ЧАТА ГПТ V

# month = int(input())
# day = int(input())

# if month < 2 or (month == 2 and day < 18):
#     print("Before")
# elif month > 2 or (month == 2 and day > 18):
#     print("After")
# else:
#     print("Special")


# swaps = input()

# ball_location = 1

# for swap_type in swaps:
#     if swap_type == "A" and ball_location == 1:
#         ball_location = 2
#     elif swap_type == "A" and ball_location == 2:
#         ball_location = 1
#     elif swap_type == "B" and ball_location == 2:
#         ball_location = 3
#     elif swap_type == "B" and ball_location == 3:
#         ball_location = 2
#     elif swap_type == "C" and ball_location == 1:
#         ball_location = 3
#     elif swap_type == "C" and ball_location == 3:
#         ball_location = 1
       
# print(ball_location)



