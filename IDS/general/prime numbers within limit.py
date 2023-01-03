def check_prime(n):
    if(n == 1):
        return 0
    for i in range (2,n):
        if(n % i == 0):
            return 0
    return 1
print("Enter start: ")
start=int(input())
print("Enter end: ")
end=int(input())
for i in range(start,end):
    if check_prime(i) and check_prime(i + 2):
        print("twin primes are:", i, i + 2)
        i = i + 1
