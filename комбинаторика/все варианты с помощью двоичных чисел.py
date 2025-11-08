w = list(map(int,input().split()))
n = [0] * len(w)


while n != [1] * len(w):
    i = len(n)-1
    while n[i] != 0:
        n[i] = 0
        i -= 1
    n[i] = 1
    print(n)