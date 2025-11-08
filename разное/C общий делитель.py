a, b, k = map(int,input().split())
q = []
for i in range(1,a+1):
    if a % i == 0 and b % i == 0:
        q.append(i)
q = q[::-1]
print(q[k-1])