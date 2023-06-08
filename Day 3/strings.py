def main():
    s = "Hello World!"
    print(s[:6])

    for c in s:
        print(c)

    s2 = (s + " ") * 3
    print(s2)

    print(s.lower(), s.upper())

    l = s.split(" ")
    print(l)

    groceries = "Apples, Oranges, Bananas"
    print(groceries.split(", "))

    print(" - ".join(l))


    groceries = groceries.replace("Apples", "Chocolate")
    print(groceries)

    print(len(s))

    if "Hello" in s:
        print("Hello in s")

main()