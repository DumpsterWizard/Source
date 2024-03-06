initial_pin = "0123"

for i in range(3):
    pincode = input("Enter your PIN code please: ")
    if len(pincode) == 4 or len(pincode) == 6:
        if pincode == initial_pin:
            print("Pincode is valid!")
            break
        else:
            print("Your PIN code is incorrect!")
    else:
        print("Sorry, pin should be 4 digits!")

print("Good bye!")