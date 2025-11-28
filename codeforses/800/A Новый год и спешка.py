n, k = map(int,input().split())
v = (4*60)-k
i = 1

while v >= 5*i and i <= n:
    v-=5*i
    i+=1

print(i-1)
