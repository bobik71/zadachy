n = int(input())
maxv = 0
nom = 0
k = []
for i in range(n):
    k.append(list(map(int,input().split())))
maxk = k [0][0]
for i in range(len(k)):
    if k[i][0] > maxk and k[i][1] == 1:
        maxk = k[i][0]
        nom = i
print(nom)


