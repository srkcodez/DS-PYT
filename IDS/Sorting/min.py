l1 = []
for i in range(5):
    l1.append(int(input()))

min=l1[0]
for i in range(5):
    if l1[i] < min:
        min=l1[i]
print(min)

