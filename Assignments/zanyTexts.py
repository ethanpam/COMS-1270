#Ethan Tan Phuc Pham          9-2-2025            COMS-1270 Section 4
#Assignment 1
#Zany Texts! Zany Text is a fun interactive game where the indivdual inputs word into already formed sentences to make a quirky fun sentence altogether.

print("Zany Text")
print("By: Ethan Pham")
print("[COMS 1270 Section 4]\n")

print("Zany Text #1")

noun1 = input("Please enter a noun: ")
adjective1 = input("Enter adjective 1: ")
adjective2 = input("Enter adjective 2: ")
adjective3 = input("Enter adjective 3: ")
place = input("Enter a place: ")
superpower = input("Enter a superpower: ")

print(f"\nOnce upon a time there was a {noun1} demon king. He was {adjective1}, {adjective2}, {adjective3} and lived in the land called {place}. With his reputation and his power of {superpower}, he ruled the land for centuries as he longed for someone worthy to defeat him.")

while True:
    user_input = input("\nType 'ENTER' to continue... ")
    if user_input == "ENTER":
        break

heroName = input("Enter the hero's name: ")
while True:
    heroGender = input("Enter the hero's gender (m) or (f): ") #Not efficient if I want capitals but it works in a way I structure it
    if heroGender == "m":
        gender = "male"
        genderSubject = "he" 
        genderPronoun = "his"
        break
    if heroGender == "f":
        gender = "female"
        genderSubject = "she"
        genderPronoun = "her"
        break    
        
villageName = input("Enter a village name: ")

print("One day, a young" + " " + gender, "adventurer named", heroName, "lived in a deserted village named " + villageName + ". Unlike many other adventurers,", heroName, "spent many years training to defeat the demon king. The demon king soon heard whispers of " + heroName + " and unleashed his army towards", villageName)

while True:
    user_input = input("\nType 'ENTER' to continue... ")
    if user_input == "ENTER":
        break 

hiddenPower = input("Please input a power: ")
print(f"Soon the land between {villageName} and {place} would clash. It would be faced with countless of fatalities and injuries. As the battle raged forward, {heroName} couldn't handle it and began advancing towards the Demon King himself. With all {genderPronoun} might, {genderSubject} charged straight at the Demon King. A battle unleashed as the Demon King used his power of {superpower} straight at {heroName}, slicing a fatal wound in {genderPronoun} stomach. As a last minute effort, {heroName} used {genderPronoun} hidden power of {hiddenPower} to finally defeat the lord himself. Where {heroName} would succumb to {genderPronoun} injuries. Peace would return as the lord's army vanished into thin air, where {heroName} would become a legend at {villageName}.\nThe END.")

while True:
    user_input = input("\nType 'ENTER' to continue... ")
    if user_input == "ENTER":
        break

print("\nZany Text #2")

name = input("Enter a name: ")
sound = input("Enter a sound you recently heard: ")
creature = input("Enter any creature you first imagined of: ")
randomThoughts = input("Enter a random thing you might see: ")

print(f"\nLate one night, {name} was looking at books in a dusty old library. Suddenly, the lights flicked as {name} heard the sound of {sound}. {name} screamed in horror thinking it was a {creature}. But oh no, it was just {randomThoughts}. Although originally in horror, {name} was relieved that it was just a coincidence as the librarian said to be quiet.")

while True:
    user_input = input("\nType 'ENTER' to continue... ")
    if user_input == "ENTER":
        break

print("\nZany Text #3")

name = input("Please enter a name: ")
teamName = input("Enter a team name: ")
opponentTeam = input("Enter the opponent team name: ")
object = input("Enter an object you find funny: ")
attack = input("Please input a silly attack move: ")
print(f"\nOne day during an intensive volleyball rally, {name} played with passion just as normal. But instead of launching a volleyball, {name} accidentally launched a {object} instead. The referee yelled at {teamName} immediately, asking them to stop. But wait... {opponentTeam}, the opponent team actually played it, causing it to become a real match. Without hesitation both teams began to protect the {object} from hitting the ground. With {teamName} almost accepting defeat, {name} used their final move of {attack} to finally finish off {opponentTeam} and secure the win!")

while True:
    user_input = input("\nType 'ENTER' to continue... ")
    if user_input == "ENTER":
        break

print("\nZany Text #4")

name = input("Enter a name: ")
profName = input("Enter a professor name: ")
object = input("Enter an object you would less expect: ")
emotion = input("Enter an emotion: ")
color = input("Enter your favorite color: ")
pattern = input("Enter a pattern (e.g. polka dots): ")
print(f"\nOne day at Iowa State, {name} walked into COMS-1270 with full confident. But when {name} pulled out their bag and opened it, a whole bunch of {object} came out! The class began to laugh at {name}, heck even {profName}. {name} truly felt {emotion}, their face turned {color} with {pattern} patterns all over their face. In the end, {profName} said that it was just a normal day at Iowa State but {name} never showed up to class again.")

#Thanks for grading my first assignment, if your curious on why Zany Text #1 is so long, its because I didn't know if they had to be different stories. I'll use piazza next time. 