print("Enter a number:")
n=int(input())
sum = 0
for x in range(1, n):
    if n % x == 0:
        sum += x
if sum == n:
    print("perfect")
else:
    print("not perfect")
