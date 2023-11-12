import random
Question = input("Ask a question!")
num = random.randint(1, 9)
if num == 1:
  print("Yes - definitely.")
elif num == 2:
  print("It is decidedly so.")
elif num == 3:
  print("Reply hazy, try again.")
elif num == 4:
  print("Ask again later.")
elif num == 5:
  print("Better not tell you now.")
elif num == 6:
  print("My sources say no.")
elif num == 7:
  print("Outlook not so good.")
elif num == 8:
  print("Without a doubt.")
elif num == 9:
  print("Very doubtful.")
else:
  print("ERROR")