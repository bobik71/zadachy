n = int(input())
q = []
for i in range(n):
    q.append((list((map(int,input().split())))))

for i in range(n):
    for j in range(n):
        if i != j:    
            print(q[i][0],q[i][1],q[j][0],q[j][1])