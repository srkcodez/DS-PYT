elements=[10,20,30,40,50]
i=0
j= len(elements)-1
pivot=65
while i<j:
    mid =  ( i + j )//2
    print(mid)
    if pivot == elements[mid]:
        print("element found")
        break
    else:
        if pivot > elements[mid]:
            i=mid+1
        else:
            j=mid-1

