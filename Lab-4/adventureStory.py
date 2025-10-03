# Ethan Pham        9-25-25        Lab B
# This interactive story has a bunch of hidden stories depending on your input
def main():
    print("Welcome to the Adventure Story!\nBy: Ethan Pham\n")
    while True:
        statement = input("You find yourself in an intensive playing volleyball as middle blocker.\nWith the opponent's team setting up a spike, do you\n[1]Help left side block\n[2]Help right side block\n[3]Do nothing and pray your teammates block\n")
        if statement == "1":
            print("Oh no, the opponent was a left side hitter, causing you to lose the point.")
            while True:
                print("\nTRY AGAIN")
                tryagain = str(input("[y]es, [n]o\n"))
                if tryagain == "y":
                    break
                if tryagain == "n":
                    return
        if statement == "2":
            print("Congratulation, with the help with you and your teammate, you were able to block and score a point with the roof technique")
            break
        if statement == "3":
            print("Believing in your teammate ability to block, the left side hitter spikes the ball through your defense, causing you to lose the point.")
            while True:
                print("\nTRY AGAIN")
                tryagain = str(input("[y]es, [n]o\n"))
                if tryagain == "y":
                    break
                if tryagain == "n":
                    return
    while True:
        statement = input("You finally rotated and now it is your turn to serve the ball. What do you do?\n[1]Float serve\n[2]Jump Serve\n[3]Underhand serve\n[4]Overhand serve\n")
        if statement == "1":
            print("With the crowd cheering you on, you toss the ball without spin. With your wrist firm as a stick you contact the ball with your palm causing the ball to move unpredictably")
            break
        if statement == "2":
            print("With the crowd cheering you on, you begin your three step approach. Finally jumping and MISSING the ball entirely, causing the ball to land on top of your face while breaking your ankles from the fall.")
            while True:
                print("\nTRY AGAIN")
                tryagain = str(input("[y]es, [n]o\n"))
                if tryagain == "y":
                    break
                if tryagain == "n":
                    return
        if statement == "3":
            print("With the crowd cheering you on, you remember the classic underhand serve, the one that mom taught you as a kid. With memories of volleyball before mom's passing, you hit the ball way up in the air causing the opponent to be blinded from the lights and misread the ball")
            break
        if statement == "4":
            print("With the crowd cheering you on, you toss the ball above your head before hitting the ball with a forward spin. It hits your teammates head before ricocheting off into your coaches face.")
            while True:
                print("\nTRY AGAIN")
                tryagain = str(input("[y]es, [n]o\n"))
                if tryagain == "y":
                    break
                if tryagain == "n":
                    return
    print("With that serve, you finally won the game while also having fun!")
if __name__ == "__main__":
    main()