def LinearSearch(a, ele):
    for i in range(len(a)):
        if a[i] == ele:
            return i + 1
    return -1


print(LinearSearch([10, 20, 30, 40], 20))
