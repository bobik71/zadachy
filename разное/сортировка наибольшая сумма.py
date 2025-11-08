n = int(input())
s = 0
k = 0
h = 0
for i in range(n):
    n1,n2,n3 = map(int,input().split())
    if n2 > k:
        k = n2
        s = n3
        h = i
print(s,h+1)
