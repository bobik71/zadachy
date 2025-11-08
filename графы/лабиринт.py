lab = [[1, 0, 1, 1, 1, 1, 1, 1],
       [1, 0, 1, 0, 0, 0, 0, 1],
       [1, 0, 1, 1, 0, 1, 0, 1],
       [1, 0, 0, 0, 0, 1, 0, 1],
       [1, 1, 1, 0, 1, 1, 0, 1],
       [1, 0, 1, 0, 1, 1, 0, 1],
       [1, 0, 0, 0, 0, 1, 0, 1],
       [1, 1, 1, 1, 1, 1, 0, 1]]

nx = 0
ny = 1
mx = 7
my = 6

a1 = [nx]
a2 = [ny]
pr = []
for i in range(8):
    pr.append([None]*8)
pr[nx][ny] = (0, 0)

steps = [0]

vis = []
for i in range(8):
    vis.append([False]*8)
vis[nx][ny] = True

while a1:
    k1 = a1.pop(0)
    k2 = a2.pop(0)
    step_n = steps.pop(0)

    if k1 == mx and k2 == my:
        print(step_n)
        break

    for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
        nxn = k1 + dx
        nyn = k2 + dy
        if 0 <= nxn < 8 and 0 <= nyn < 8:
            if lab[nxn][nyn] == 0 and not vis[nxn][nyn]:
                a1.append(nxn)
                a2.append(nyn)
                pr[nxn][nyn] = (k1, k2)
                steps.append(step_n + 1)
                vis[nxn][nyn] = True


p = []
while True:
    p.append((mx,my))
    mx = pr[mx][my][0]
    my = pr[mx][my][1]
    if mx == 0 and my == 0:
        break
p.append((nx,ny))

for i in range(len(p)-1,-1,-1):
    print(p[i], end = ' ')
    


