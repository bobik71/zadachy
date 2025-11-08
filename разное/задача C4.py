a, b, c = map(int,input().split())
for i in(a,b,c):
    for j in(a,b,c):
        for k in(a,b,c):
            if i != j and k != j and i != j and i != k:
                print(i, j, k)