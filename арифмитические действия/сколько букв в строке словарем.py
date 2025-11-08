sl = {}
s = input()
t = 'qwertyuiopasdfghjklzxcvbnm'
for i in t:
    sl[i] = 0

for i in s:
    sl[i] += 1

for i in range(len(t)):
    print(t[i],' - ', sl[t[i]])