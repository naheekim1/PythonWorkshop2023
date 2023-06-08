def main():
    coolNumbers = {3, 6, 4, 10, 2, 3}
    print(coolNumbers)

    charactersInS = set("Hello World!")
    print(charactersInS)

    if "h" not in charactersInS:
        print("Sorry, only H is in charactersInS")
    
    cis1 = charactersInS
    cis2 = {c for c in "Hello World2"}

    print(cis1)
    print(cis2)

    print(cis1 | cis2)
    print(cis1 & cis2)
    print(cis1 - cis2)
    #Symmetric difference ^
    #Subsets <=
    #Supersets >=
main()