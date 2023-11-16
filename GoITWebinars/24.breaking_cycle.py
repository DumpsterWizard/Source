string = 'break statement'

for letter in string:
    print(letter)

    if letter == 'e' or letter == 's':
        break

print('Out of the loop')


string = 'break statement'

for letter in string:

    if letter == 'e' or letter == 's':
        print(letter)
        continue

    print('space', letter)

print('Out of the loop')

string = 'break statement'

for letter in string:

    if letter == 'e' or letter == 's':
        pass

    print(letter, end=' ')

print('Out of the loop')
# ___________________________________________________________

for letter in 'continue statement':

    if letter == 'n' or letter == 't':
        continue
    else:
        print(letter, end=' ')


print('Out of the loop')
# ______________________________________________________________

maximum = 11

for element in range(1, maximum+1):
    for i in range(10):
        if i == 5:
            break
        print('not enough')

    print('pass')
