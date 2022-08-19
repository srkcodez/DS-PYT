start = int(input("enter beginning "))
end = int(input("enter ending"))
for n in range(start, end):
    count = 0
    for i in range(2, n):
        if n % i == 0:
            count = 1
            break
    if count == 0:
        print(n)
