n = list(map(int,input().split()))

for i in range(len(n)):
    for j in range(i+1,len(n)):
        for t in range(j+1,len(n)):
            print(n[i], n[j], n[t])