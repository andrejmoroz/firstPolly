a = input()
b = input()
c = []
m = len(b)
for i in a:
    if i in c:
        continue
    for j in b:
        if i != j in range(0, m+1):
            c.append(i)
            break
print(c)