l = []
print("Enter n value:")
n = int(input())
print("Enter the list:")
for i in range(0, n):
    j = int(input())
    l.append(j)
print("Enter the element to search:")
x = int(input())
for i in range(0, n):
    if x == l[i]:
        print("The element is present in the list:")
        break
    if i == n:
        print("The element is not present in the list:")
