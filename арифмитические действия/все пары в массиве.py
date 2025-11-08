q = (list((map(int,input().split()))))
for i in range(len(q)):
    for j in range(len(q)):
        if i != j:
            print(q[i],q[j])