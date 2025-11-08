c = input()
s = input()
p = c

for i in range(len(s)):
    if s[i] > p[0]:
        p += s[i]
    else:
        p = s[i] + p

print(p)