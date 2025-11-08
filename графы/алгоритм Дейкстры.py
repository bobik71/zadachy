from queue import PriorityQueue

def destr(q):
    pq = PriorityQueue()
    a = [0]*(n+1)
    b = [1000000]*(n+1)
    b[q] = 0
    pq.put((0,q))
    while not pq.empty():
        r, g = pq.get()
        if r > b[g]:
            continue
        a[g] = 1
        for i in range(len(s[g])):
            if a[s[g][i][1]] == 0:
                r1 = r + s[g][i][0]
                if b[s[g][i][1]] > r1:
                    b[s[g][i][1]] = r1
                    pq.put((r1, s[g][i][1]))
    #print(b)
    return b[1:n+1]
                


n = int(input())
m = int(input())
s = {}
for i in range(n+1):
    s[i] = []
for i in range(m):
    a,b = map(int,input().split()) 
    w = int(input())
    s[a].append((w,b))
    s[b].append((w,a))
   
print(*destr(1))