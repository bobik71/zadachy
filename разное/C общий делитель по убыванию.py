a, b, k = map(int,input().split())
s = 0
for i in range (a,0,-1):
    if a % i == 0 and b % i == 0:
        s = s + 1
    if s == k:
        print(i)
        exit()
