n, k = map(int,input().split())
h = []
s = 0
maxi = 0
h = list(map(int,input().split()))
for i in range(n):
    if h[i] > maxi:
        maxi = h[i]
        nom = i
h[nom] = 0
maxi1 = 0
for i in range(n):
    if h[i] > maxi1:
        maxi1 = h[i]
        nom1 = i
h[nom1] = 0
maxi2 = 0
for i in range(n):
    if h[i] > maxi2:
        maxi2 = h[i]
        nom2 = i
h[nom2] = 0

print(nom, nom1, nom2)
