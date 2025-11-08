s = input()
p = []
t = 0
for q in range(1072,1105):
    f = chr(q)
    p.append(t)
    t = 0
    for i in range(len(s)):
        if s[i] == f:
            t+=1
m = p[0]
for i in range(len(p)):
    if p[i] > m:
        m = p[i]
        k = i
a = 1072 + k - 1
a1 = chr(a)
print('больше всего букв -',a1, 'их',m)
        