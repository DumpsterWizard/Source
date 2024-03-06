# for i in range(1, 21):
#     if i == 4 or i == 13:
#         print(f"{i} is unlucky!")
#     elif i % 2 == 0:
#         print(f"{i} Is even")
#     else:
#         print(f"{i} is odd")


for i in range(1, 21):
    if i == 4 or i == 13:
        status = "Unlucky"
    elif i % 2 == 0:
        status = "Even"
    else:
        status = "Odd"
    print(f"{i} is {status}!")