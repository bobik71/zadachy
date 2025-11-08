n = input()
b = 0
l = len(n)
for i in range(l):
    a = n[i]
    if a in '6 9 0':
        b = b + 1  
    elif a == '8':
        b = b + 2  
print(b)

