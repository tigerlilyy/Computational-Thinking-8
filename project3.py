cow = 0
pig = -5
sheep = 1
rat = 0

print("Hi this project will tell you if you are a cow or a pig or a sheep")
print("so after this project you will ether go:")
print(" ")
print("baaaaa")
print("  ")
print("oink")
print(" ")
print(" or")
print(" ")
print("moooo")
print("okay lets start")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
answer1 = input("do you like farm or city more?    ")
if answer1 == "farm":
    cow += 2
    pig += 4
    sheep += 2
elif answer1 == "city":
    print("bad answer this is about farm animals.")
    rat += 1
else:
    print("bro what even is that")
    rat += 11

answer2 = input("do you like white, gray, black, or pink the most?     ")
if answer2 == "white":
    print("okay okay you are basic.")
    sheep += 2
elif answer2 == "gray":
    rat += 1
elif answer2 == "black":
    cow += 1
elif answer2 == "pink":
    pig += 1
else:
    print("actually what ")
    rat += 11
answer3 = input("do you like pizza, cotton candy, milk, or ice cream the most?  ")
if answer3 == "pizza":
    print("ew")
    rat += 1
elif answer3 == "cotton candy":
    pig += 3
    sheep += 1
elif answer3 == "milk" or answer3 == "ice cream":
    cow += 1
else:
    print("  ")
    print("weirdo")
    rat += 11

answer4 = input("when you die do you believe in being reincarnated? yes or no:   ")
if answer4 == "yes" or answer4 == "Yes":
    sheep += 1
    cow += 1
elif answer4 == "no" or answer4 == "No":
    pig += 1
else:
    print("why would you write such a weird answer.")
    rat += 11

answer5 = input("do you like hamburgers, pork, chicken or lamb most?   ")
if answer5 == "hamburger" or answer5 == "hamburgers":
    cow -= 1
elif answer5 == "pork":
    pig -= 1
elif answer5 == "chicken":
    rat += 1
elif answer5 == "lamb":
    sheep -= 2
else:
    print("what.")
    rat += 58729


answer6 = input("what is our lucky number out of these? 10, 3, 20,000, or 1?    ")
if answer6 == "10":
    cow += 1
elif answer6 == "3":
    pig += 2
elif answer6 == "20,000" or answer6 == "20000":
    sheep += 1
elif answer6 == "1":
    rat += 1

else:
    rat += 10


print(f" your scores are {cow} cow points, {pig} pig points, {sheep} sheep points. BUT WAIT. there was also a secret variable.... RAT")
print("it is easiest to get sheep and hardest to get pig. actually it is easiest to get rat ")
print(f" you had {rat} rat points. ")

#this one is if ou answer most things that add up to pig points
if pig > sheep and pig > cow and pig > rat:
    print("wowowowo you got pig!!! thats the hardest to get crazyyyy")
#this ending is for sheep 
elif sheep > pig and sheep > cow and sheep > rat:
    print("yay you got sheep my favorite!")
elif cow > sheep and cow > pig and cow > rat:
    print("yay you are cow! you contribute to climate change with your nasty nasty burps")
elif rat > sheep and rat > pig and rat > cow:
    print("EEEWWWWWW you are nasty nasty rat. you proobablyyy got this by answering a lot of question with random answers or you answered gray, pizza, or 1. ")
# these endings are for if you are tied with two of the animals
elif pig == sheep:
    print("you are tied with pig and sheep")
elif pig == cow:
    print("you are tied between pig and cow")
elif cow == sheep:
    print("you are tied between cow and sheep!!")
# this is if something did happen to go wrong or something
else:
    print("You are kinda weird and idk your score.")