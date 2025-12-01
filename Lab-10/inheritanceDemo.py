# Matthew Holman             4-27-2023
# COM S 1270 - Inheritance Demo

class Animal:
    def __init__(self, name, age, color, cost) -> None:
        self.name = name
        self.age = age
        self.color = color
        self.cost = cost
    
    def __str__(self) -> str:
        return ("Name: " + str(self.name) + 
                ", Age: " + str(self.age) +
                ", Color: " + str(self.color) +
                ", Cost: " + str(self.cost))
    
    def speak(self) -> str:
        return "Hello"

class Cat(Animal):    
    def speak(self) -> str:
        return "Meow!" * self.age

class Dragon(Animal):    
    def speak(self) -> str:
        return "Hiss" + ("." * self.age)

class Werewolf(Animal):
    def speak(self) -> str:
        return "G" + ("r" * self.age)

class Robot:
    def __init__(self, power) -> None:
        self.power = power
    
    def beep(self) -> str:
        return "beep " * self.power

class Tiger(Cat, Robot):
    def __init__(self, name, age, color, cost, strength, power) -> None:
        Cat.__init__(self, name, age, color, cost)
        Robot.__init__(self, power)
        self.strength = strength
    
    def __str__(self) -> str:
        return super().__str__() + ", Strength: " + str(self.strength)
    
    def yell(self) -> str:
        return ("Roar" + "!" * self.strength) * self.age
        

def main():
    c1 = Cat("Whiskers", 4, "Brown", 5000)
    print(c1.speak())
    
    d1 = Dragon("Puff", 30, "Blue", 350)
    print(d1.speak())
    
    w1 = Werewolf("Remus", 35, "Black", 1000)
    print(w1.speak())
    
    t1 = Tiger("Tony", 21, "Orange", 275, 5, 9)
    print(t1.beep())
    
    print()
    
    animals = []
    animals.append(c1)
    animals.append(d1)
    animals.append(w1)
    animals.append(t1)
    
    for animal in animals:
        print(animal.speak())
    

if __name__ == "__main__":
    main()