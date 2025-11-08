n = int(input())
m = int(input())
s1 = [0]*(n+1)
s = []
for i in range(n+1):
    s.append(s1.copy())
for i in range(m):
    a,b = map(int,input().split())
    s[a][b] += 1
    s[b][a] += 1
for i in range(n):
    print(s[i])