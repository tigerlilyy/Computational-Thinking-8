import random

character_list = ["Lorelai","Rory","Christopher", "Emily","Dean", "Luke", "Jess", "Logan", "Lane", "Sookie", "Paris", "Kirk", "Richard"]
character = random.choice(character_list)

 # print(f"{character}")

for i in range(5):
    guess = input("Guess a character from Gilmore Girls:   ")
    if guess == character:
        print("you win! yayyyy")
        print()
        print(f"You guessed right, it was {character}!!!!!")
        quit()

    if i == 0:
        if character == "Lorelai" or character == "Rory" or character == "Emily" or character == "Lane" or character == "Sookie" or character == "Paris":
            print("the character is a girl")
        else:
            print("the character is a guy")
    if i == 1:
        if character == "Lorelai":
            print("she loves coffee")
        elif character == "Rory":
            print("she is quieter than others")
        elif character == "Emily":
            print("she is super annoying")
        elif character == "Lane":
            print("she is rebellious")
        elif character == "Sookie":
            print("she has a son")
        elif character == "Paris":
            print("she is kind of annoying")
        elif character == "Dean":
            print("he is divorced")
        elif character == "Luke":
            print("he has a boat")
        elif character == "Logan":
            print("he likes partying")
        elif character == "Jess":
            print("he kind of dissapeared at the end of the series")
        elif character == "Richard":
            print("the character retired at one point")
        elif character == "Kirk":
            print("everyone lowkey loves and hates him ")
        elif character == "Christopher":
            print("he has two kids")
    if i == 2:
        if character == "Lorelai":
            print("she is brunette")
        elif character == "Rory":
            print("she brunette")
        elif character == "Emily":
            print("shes brunette")
        elif character == "Lane":
            print("she has black hair ")
        elif character == "Sookie":
            print("she has brown/red hair")
        elif character == "Paris":
            print("she has blonde hair")
        elif character == "Dean":
            print("he is brunette")
        elif character == "Luke":
            print("he is brunette")
        elif character == "Logan":
            print("he is blonde")
        elif character == "Jess":
            print("he is brunette")
        elif character == "Richard":
            print("he has graying hair")
        elif character == "Kirk":
            print("he has light brown hair")
        elif character == "Christopher":
            print("he is brunette")
print("oh noooo you ran out of guesses..... YOU LOSE")
print()
print(f"the character was {character}! but you didn't guess them so HAHA TOO BAD")