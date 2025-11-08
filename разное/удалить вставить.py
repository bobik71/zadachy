s = input()
s = list(s)
q = s[0]
del s[0]
print(s)
s.insert(0,q)
print(s)