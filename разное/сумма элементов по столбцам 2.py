s1 = 0
s2 = 0
s3 = 0
s4 = 0

for i in range(5):
    a, b, c, d = map(int,input().split())
    s1 += a
    s2 += b
    s3 += c
    s4 += d

print(s1,s2,s3,s4)
