def main():
    shop = {"Apples":3, "Oranges":4.25, "Peaches":3.99}
    print(shop["Apples"])
    
    shop["Bananas"] = 3.50
    print(shop)

    if "Oranges" in shop:
        print("Oranges:", shop["Oranges"])

    del shop["Peaches"]
    print(shop)

    for fruit in shop:
        print(fruit)

    squares = {i:i**2 for i in range(1,21)}
    print(squares)

main()