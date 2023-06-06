def main():
    x = [1, 6, 3, 4, 5]
    x[1] = 2
    print(x[3])
    print(x[0:2])
    print(x[::2])
    print(x[1::2])
    print(x[-2:])
    print(x[::-1])

    for i in x:
        print(i)

    if 2 in x:
        print("Yes")
    if not 6 in x:
        print("No")

main()