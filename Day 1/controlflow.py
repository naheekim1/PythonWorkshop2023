def main():
    # ==
    # !=
    # >
    # <
    # >=
    # <=

    print("Is 5 less than 10 AND greater than 4?:", 5 < 10 and 5 > 4)
    print("Is 5 greater than 10 OR less than 4?:", 5 > 10 or 5 < 4)
    print("Is 5 NOT greater than 10?:", not 5 > 10)

    x = float(input("Input the number 5: "))

    if x > 5:
        print("sorry, that number is too big")
    elif x < 5:
        print("sorry, that number is too small")
    else:
        print("Yay! You did it!!!")


main()