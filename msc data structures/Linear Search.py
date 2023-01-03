def LinearSearch(elements, pivot):
    # elements contain data items to be searched
    # pivot is the element that we are about to search
    for i in range(len(elements)):  # picking the next element form the data items list
        if elements[i] == pivot:  # comparting next element with pivot element
            return i  # if element matches with data times return position

    return -1  # return negitive to calling function to indicate element is not present


pos = LinearSearch(["aries", "taurus", "gemini", "cancer"], "gemini")

if pos != -1:
    print("element present at: ", pos + 1)
else:
    print("element not present")

pos = LinearSearch([14, 12, 13, 19], 14)

if pos != -1:
    print("element present at: ", pos + 1)
else:
    print("element not present")
