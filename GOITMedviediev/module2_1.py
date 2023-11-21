initial_pin = "0123"
max_tries = 3

n = 0
while n < max_tries:
    pincode = input("Enter your PIN code please: ")
    if len(pincode) >= 4:
        if pincode == initial_pin:
            amount = int(input("How much money do you want: "))
            if amount > 0:
                print(f"Take your {amount} $")
                break
        else:
            print("Your PIN code is incorrect! Try again")
            print(f"You have {max_tries - n - 1} tries left!")
            n += 1

    else:
        print("Sorry, pin should be 4 digits!")
        print(f"You have {max_tries - n - 1} tries left!")
        n += 1

print("Good bye!")

