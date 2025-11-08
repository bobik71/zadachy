a, b = map(int,input().split())
for i in range(1,a):
    if a % i == 0 and b % i == 0:
        s = i
e = a * b // s
print(s,e)