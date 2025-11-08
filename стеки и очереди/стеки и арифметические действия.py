a = input()
a1 = []
for i in a:
    if i == '+' or i == '-' or i == '*' or i == '/':
        k1 = int(a1.pop())
        k2 = int(a1.pop())
        if i == '+':
            a1.append(k1+k2)
        if i == '-':
            a1.append(k1-k2)
        if i == '*':
            a1.append(k1*k2)
        if i == '/':
            a1.append(k1//k2)
    else:
        a1.append(i)
print(*a1)