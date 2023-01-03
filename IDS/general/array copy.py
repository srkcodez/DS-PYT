lst1 = []
lst2 = []
n = int(input("Enter number of elements : "))

for i in range(0, n):
    ele = int(input())
    lst1.append(ele)
print(lst1)

lst2 = lst1
#
# for i in range(0, len(lst1)):
#     lst2 = lst1
print("list 2 is")
print(lst2)
