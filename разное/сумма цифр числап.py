
def summ(a):
    s = 0
    q = []
    for i in range(1,a):
        if a % i == 0:
            q.append(i)
    s = sum(q)
    return(s)
k = int(input())
print(summ(a))