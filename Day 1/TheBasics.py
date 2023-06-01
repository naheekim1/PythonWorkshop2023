# This is our first program
"""
    Multi line comment kinda sorta not really
"""

"This is a string"

'This is also a string'
'c' #character

5 #Integers
5.1 #Float

True and False #Booleans

print("This is a print statement.\n\tThis outputs \"strings\" to the terminal")
print("This is a second \\ line.")

"\\\\\\" # is 3 back slashes

x = input("Enter a number: ")
x = int(x)
print("Here is your number +1 : ", x + 1, sep="")
print()

print("This is a", end=" ")
print("complete sentence")

inp = float(input("Enter a floating point number: "))
print("Here is the square of your number:", inp ** 2)

print("5 / 2 =", 5/2)
print("5 / 2 as an integer is", 5//2)
print("5 / 2 gives a remainder of", 5 % 2)
print("-5 % 3 =", -5 % 3)

print("You are #" + str(1))

print(type(""), type(1), type(2.6), type(True))

print(1)
print(2)