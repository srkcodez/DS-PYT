print("Enter two values:")
x = int(input())
y = int(input())
# choose the smaller number
if x > y:
    smaller = y
else:
    smaller = x
for i in range(1, smaller + 1):
    if (x % i == 0) and (y % i == 0):
        gcd = i
print("The GCD is", gcd)

if x > y:
    greater = x
else:
    greater = y
while True:
    if (greater % x == 0) and (greater % y == 0):
        lcm = greater
        break
    greater += 1
print("LCM is:", lcm)
