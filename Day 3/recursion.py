def sumUpTo(n):
    if n == 1:
        return 1
    return n + sumUpTo(n-1)

def gcd(a, b):
    if a == 0: 
        return b
    if b == 0: 
        return a
    return gcd(b, a % b)

def main():
    print(sumUpTo(3))
    print(gcd(4, 20))
main()