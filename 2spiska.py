a = input()
b = input()
a = list(set(a))
b = list(set(b))
c = list()
n = len(b)
for i in a:
    for j in b:
        if i not in b:
            if i in c:
                continue
            c.append(i)
            break
print(c)
