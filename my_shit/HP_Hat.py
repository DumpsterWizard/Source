print("====================")
print("=====SORTINGHAT=====")
print("====================")

gryffindor = 0
ravenclaw = 0
hufflepuff = 0
slytherin = 0

print("Do you like Dawn or Dusk? \n1) Dawn \n2) Dusk")
answer = int(input("Give me your answer, kiddo! (Type 1 or 2!) \n"))
if answer== 1:
    gryffindor += 1
    ravenclaw += 1
elif answer== 2:
    hufflepuff +=1
    slytherin +=1
else:
    print("I need straight answers, brat!")

print("When you're dead, you want people to remember you as: \n1) The Good \n2) The Great \n3) The Wise \n4) The Bold")
answer = int(input("Tell me right away! (Type 1 or 2 or 3 or 4) \n"))
if answer == 1:
    hufflepuff +=2
elif answer == 2:
    slytherin +=2
elif answer == 3:
    ravenclaw +=2
elif answer == 4:
    gryffindor +=2
else:
    print("Dude, how difficult is that?...")

print("Which kind of instrument most pleases your ear? \n1) The violin \n2) The trumpet \n3) The piano \n4) The drum")
answer = int(input("So, what's it's gonna be? (Speak the number, from 1 to 4!) \n"))
if answer == 1:
    slytherin +=4
elif answer == 2:
    hufflepuff += 4
elif answer == 3:
    ravenclaw += 4
elif answer == 4:
    gryffindor += 4
else:
    print("Just pick a number!") 


most_points = max(slytherin, hufflepuff, ravenclaw, gryffindor)

if slytherin == most_points:
    print("🐍REPTILE WINS🐍")
if hufflepuff == most_points:
    print("🦡FOKIN BADGERS🦡")
if gryffindor == most_points:
    print("🦁THE GOLDEN LIONS🦁")
if ravenclaw == most_points:
    print("🦅BIRD IS THE BIRD🦅")