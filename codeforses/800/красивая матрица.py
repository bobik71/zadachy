mat = []
i1 = 0
j1 = 0
s = 0
for i in range(5):
    mat.append(list(map(int,input().split())))
    
for i in range(5):
    for j in range(5):
        if mat[i][j] == 1:
            i1 = i+1
            j1 = j+1
            
while (i1 != 3) or (j1 != 3):
    if i1 < 3:
        i1 += 1 
        s += 1 
    elif i1 > 3:
        i1 -= 1 
        s += 1 
    elif j1 < 3:
        j1 += 1 
        s += 1 
    elif j1 > 3:
        j1 -= 1 
        s += 1 
        
print(s)

