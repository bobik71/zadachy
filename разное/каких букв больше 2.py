s = input()
p = []
t = 0
t1 = 0
for q in range(1072,1105):
    f = chr(q)
    t = 0
    for i in range(len(s)):
        if s[i] == f:
            t+=1
    if t > t1:
        t1 = t
        a = f
print(t1,a)
        