DIMENSIONS = 2

def computeSquareArea(side):
    return side ** DIMENSIONS

def main():
    x = int(input("Enter the length of a square: "))
    print("The square has Area:", computeSquareArea(x), "square units")

main()

