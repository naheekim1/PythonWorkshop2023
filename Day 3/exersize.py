import random

def main():
    rn = random.randrange(1,11)

    user = int(input("Select a number: "))
    while rn != user:
        print("You're super wrong!")
        user = int(input("Select a number: "))
    print("You Win!")

main()