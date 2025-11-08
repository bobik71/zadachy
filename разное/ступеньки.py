n = int(input())
a = list(map(int,input().split()))
q = []
s = 0
for i in a:
    if a[i] < a[i+1]:
        s += 1
    else:
        q.append(s)
        s = 0
        print(q)

