print("Enter three values:")
a = int(input("Enter first number"))
b = int(input("Enter second number"))
c = int(input('Enter third number'))
print("Given values are:", a, b, c)
if (a > b) and (a > c):
    print("a is greater")
elif (b > a) and (b > c):
    print("b is greater")
else:
    print("c is greater")
