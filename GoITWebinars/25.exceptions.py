try:
    value_a = input("Enter value a: ")
    value_b = input("Enter value b: ")

    value_x = -value_a / value_b

except TypeError:
    print('Type Error exception block')
    try:
        value_x = -float(value_a) / float(value_b)
    except ValueError:
        print("Error! could not convert string to float")
    except ZeroDivisionError:
        print("Error! Couldnt divide by zero")
    else:
        print(f"Result X equal {round(value_x, 2)}")
else:
    print(f"Result X equal {round(value_x, 2)}")

finally:
    print("End of calculation")


# ________________________________________________________________
try:
    value_a = input("Enter value a: ")
    value_b = input("Enter value b: ")

    value_x = -float(value_a) / float(value_b)

except Exception as e:
    print(e)
else:
    print(f"Result X equal {round(value_x, 2)}")
finally:
    print("End of calculation")