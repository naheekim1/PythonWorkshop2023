def main():
    x = list(range(1,21))
    print(x)
    print("List length:", len(x))

    listY = x + [21, 22, 23, 24, 25]
    listZ = [1] * 20
    print(listY)
    print(listZ)
    
    listZ.append(2)
    print(listZ)
    
    listZ.remove(2)
    listZ.remove(1)
    print(listZ)

    print(listY.index(20))
    listY.insert(1, 0)
    print(listY)

    del x[0:5]

    print(x)

    print(max(1, 2))
    print(min(1, 2, 3))

    print(min([1, 2, 3]))

    #List comprehension
    listA = [1, 2, 3, 4, 5]

    listB = []
    for i in listA:
        listB.append(i ** 2)

    print(listB)

    listC = [i**2 for i in listA]
    print(listC)

    listD = [i-1 for i in listA]
    print(listD)

    listE = [i ** 2 for i in range(1,6) if i % 2 == 1]
    print(listE)

main()