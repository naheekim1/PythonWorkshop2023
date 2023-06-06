def main():
    for i in range(10):
        print(i)

    print("---------------")

    for i in range(3, 10):
        print(i)

    print("---------------")

    for i in range(3, 10, 2):
        print(i)
        
    # range(end) assumes start = 0 and increment = 1
    # range(start, end) assumes increment = 1
    # range(start, end, increment) assumes nothing

main()

"""
for (int i = 3; i < 10; i+=2) {
    cout << i << endl;
}
"""