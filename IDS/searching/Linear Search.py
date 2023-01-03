def LinearSearch(a, ele):
    for i in range(len(a)):
        if a[i] == ele:
            return i + 1
    return -1


def BinarySearch(a, ele):
    low = 0
    high = len(a)-1
    while low <= high:
        mid = (low + high) // 2
        print(low, high, mid)
        if a[mid] == ele:
            return mid
        elif a[mid] < ele:
            low = mid + 1
        elif a[mid] > ele:
            high = mid - 1

    return -1


print(LinearSearch([10, 20, 30, 40], 20))

print(BinarySearch([32, 41  ,53, 76, 92, 141], 92))
