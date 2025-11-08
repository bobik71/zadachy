nx1, ny = map(str,input().split())
ny = int(ny)
nx = ord(nx1) - 96
mx1, my = map(str,input().split())
my = int(my)
mx = ord(mx1) - 96

desk = []
for i in range(10):
    desk.append([0]*10)

desk1 = []
for i in range(10):
    desk1.append([0]*10)

desk2 = []
for i in range(10):
    desk2.append([0]*10)


desk[nx][ny] = 1
desk1[nx][ny] = -1
desk2[nx][ny] = -1

a1 = []
a2 = []
a1.append(nx)
a2.append(ny)

while True:
    x = a1.pop(0)
    y = a2.pop(0)
    k = desk[x][y]
    if x+1 <= 9 and y+2 <= 9:
        if desk[x+1][y+2]==0:
            a1.append(x+1)
            a2.append(y+2)
            desk1[x+1][y+2] = x
            desk2[x+1][y+2] = y
            desk[x+1][y+2]=k+1
            if x+1 == mx and y+2 == my:
                print(k)
                break
    if  x-1 >= 1 and y-2 >= 1: 
        if desk[x-1][y-2]==0:
            a1.append(x-1)
            a2.append(y-2)
            desk1[x-1][y-2] = x
            desk2[x-1][y-2] = y
            desk[x-1][y-2]=k+1
            if x-1 == mx and y-2 == my:
                print(k)
                break
    if x+1 <= 9 and y-2 >= 1: 
        if desk[x+1][y-2]==0:
            a1.append(x+1)
            a2.append(y-2)
            desk1[x+1][y-2] = x
            desk2[x+1][y-2] = y
            desk[x+1][y-2]=k+1
            if x+1 == mx and y-2 == my:
                print(k)
                break
    if x-1 >= 1 and y+2 <= 9:
        if desk[x-1][y+2]==0:
            a1.append(x-1)
            a2.append(y+2)
            desk1[x-1][y+2] = x
            desk2[x-1][y+2] = y
            desk[x-1][y+2]=k+1
            if x-1 == mx and y+2 == my:
                print(k)
                break
    if x+2 <= 9 and y+1 <= 9:
        if desk[x+2][y+1]==0:
            a1.append(x+2)
            a2.append(y+1)
            desk1[x+2][y+1] = x
            desk2[x+2][y+1] = y
            desk[x+2][y+1]=k+1
            if x+2 == mx and y+1 == my:
                print(k)
                break
    if x-2 >= 1 and y-1 >= 1:
        if desk[x-2][y-1]==0:
            a1.append(x-2)
            a2.append(y-1)
            desk1[x-2][y-1] = x
            desk2[x-2][y-1] = y
            desk[x-2][y-1]=k+1
            if x-2 == mx and y-1 == my:
                print(k)
                break
    if x+2 <= 9 and y-1 >= 1:
        if desk[x+2][y-1]==0:
            a1.append(x+2)
            a2.append(y-1)
            desk1[x+2][y-1] = x
            desk2[x+2][y-1] = y
            desk[x+2][y-1]=k+1
            if x+2 == mx and y-1 == my:
                print(k)
                break
    if x-2 >= 1 and y+1 <= 9:
        if desk[x-2][y+1]==0:
            a1.append(x-2)
            a2.append(y+1)
            desk1[x-2][y+1] = x
            desk2[x-2][y+1] = y
            desk[x-2][y+1]=k+1
            if x-2 == mx and y+1 == my:
                print(k)
                break

p = []
while mx != -1 and my != -1:
    mx1 = mx
    p.append(chr(mx+96)+str(my))
    mx = desk1[mx][my]
    my = desk2[mx1][my]

for i in range(len(p)-1, -1, -1):
    print(p[i], end = ' ')
