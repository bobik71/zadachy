w = []
for i in range(int(input())):
    t = int(input())
    a = input()
    q = []
    s = 0
    s1 = 0
    

    for i in range(len(a)):
        s = 0
        if a[i] not in q:
            q.append(a[i])
            for j in a:
                if a[i] == j:
                    s+=1
        if ord(a[i])-64 <= s:
            s1 += 1
    w.append(s1)    
for i in range(len(w)):
    print(w[i])    