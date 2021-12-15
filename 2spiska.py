a = input()
b = input()
a = list(set(a))
b = list(set(b))
c = list()
for i in a:
    for j in b:
        if i not in b:
            if i in c:
                continue
            c.append(i)
            break
print(c)
