def binary_search(a, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if a[mid] == x:
            return mid

        elif a[mid] > x:
            return binary_search(a, low, mid - 1, x)

        else:
            return binary_search(a, mid + 1, high, x)

    else:
        return -1


a = []
print("Enter an array elements:")
for i in range(0, 4):
    ele = int(input())
    a.append(ele)
print("Given Array is:", a)
print("Enter search element:")
x = int(input())

# Function call
result = binary_search(a, 0, len(a) - 1, x)

if result != -1:
    print("Element is present at index", result)
else:
    print("Element is not present in array")
