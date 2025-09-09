#Ethan Tan Phuc Pham          9-2-2025            COMS-1270 Section 4
#Assignment 1
#Zany Texts! An interactive text-based adventure game

print("Zany Text!")
print("By: Ethan Pham")
print("[COMS 1270 Section 4]\n")

noun1 = input("Please enter a noun: ")
adjective1 = input("Enter adjective 1: ")
adjective2 = input("Enter adjective 2: ")
adjective3 = input("Enter adjective 3: ")
place = input("Enter a place: ")
superpower = input("Enter a superpower: ")

print(f"\nOnce a upon of time there was a {noun1} demon king. He was {adjective1}, {adjective2}, {adjective3} and lived in the land called {place}. With his reputation and his power of {superpower}, he ruled the land for centuries as he longed for someone worthy to defeat him.")

while True:
    user_input = input("\nType 'ENTER' to continue... ")
    if user_input == "ENTER":
        break

heroName = input("Enter the hero's name: ")
while True:
    heroGender = input("Enter the hero's gender (m) or (f): ") #Not efficient if I want capitals but it works
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

print("One day, a young" + " " + gender, "adventurer name", heroName, "lived in a deserted village named " + villageName + ". Unlike many other adventurers,", heroName, "spent many years training to defeat the demon king")

