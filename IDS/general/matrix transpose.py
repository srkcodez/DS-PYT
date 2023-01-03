print("Enter the no of rows and cols of a matrix:")
r = int(input())
c = int(input())
print("Enter a matrix:")
a = []
for i in range(r):
    m = []
    for j in range(c):
        ele = int(input())
        m.append(ele)
    a.append(m)
print("Given matrix is:")
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end=" ")
    print()
print("TRANSPOSE:")
t = []
for i in range(c):
    m = []
    for j in range(r):
        ele = a[j][i]
        m.append(ele)
    t.append(m)
print("Resultant matrix is:")
for i in range(len(t)):
    for j in range(len(t[i])):
        print(t[i][j], end=" ")
    print()
