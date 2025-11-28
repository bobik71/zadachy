"""t = int(input())
k = 0

for i in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    ai = None
    aj = None
    ak = None
    for j in range(1,n):
        if a[i] + a[j-1] >= a[k] and i != j-1 and i != k and j-1 != k:
            break
        for k in range(2,n):
            if a[i] + a[j] >= a[k] and i != j and i != k and j != k:
                ai = i
                aj = j
                ak = k
                print(ai, aj, ak)
                break
    if ai == None and aj == None and ak == None:
        print(-1)  """

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    found = False
    for i in range(n - 2):
        if a[i] + a[i + 1] <= a[i + 2]:
            print(i + 1, i + 2, i + 3)  # индексы 1-based
            found = True
            break
    if not found:
        print(-1)


