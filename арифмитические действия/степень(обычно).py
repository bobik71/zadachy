def step(a,b):
    m =1
    for i in range(1,b+1):
        m *= a
    return(m)

a = int(input())
b = int(input())

print(step(a,b))