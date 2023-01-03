def BinarySearch(elements, pivot):
    low = 0
    high = len(elements)-1

    while low <= high:
        mid = (low + high) // 2
        if pivot == elements[mid]:
            return mid
        elif pivot < elements[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1


pos = BinarySearch([1, 6, 3, 4, 2], 6)
if pos != -1:
    print("element is present at: ", pos + 1)
else:
    print("element not present")
