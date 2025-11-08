def cic(a):
    max = '1'
    for i in a:
        if i > max:
            max = i
    return int(max)+1
def kolvo(a):
    s = len(a)
    return s
def perevod(a):
    s = 0
    sis = cic(a)
    k = kolvo(a)
    for i in range(k-1,-1,-1):
        s += int(a[k-1-i]) * sis ** i
    return(s)

n = int(input())
s = 0
for i in range(n):
    a = input()
    s += perevod(a)
print(s)

    
    


    