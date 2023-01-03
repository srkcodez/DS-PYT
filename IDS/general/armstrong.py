sum = 0
print("enter a number")
n = int(input())
temp = n
while n > 0:
    r = n % 10
    sum = sum + r ** 3
    n = n // 10
print(int(sum))
if sum == temp:
    print("armstrong")
else:
    print("not")
