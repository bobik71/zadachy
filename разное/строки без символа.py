s = input()
s2 = list(s)
s3 = s2
k = len(s2)
for i in range(k):
    q = s2[i]
    del s2[i]
    print(''.join(s2))
    s2.insert(i,q)