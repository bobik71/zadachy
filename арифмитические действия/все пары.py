n = int(input())
s = list(map(int,input().split()))
for i in range(0,n-1):
    for j in range(i+1,n):
        print(s[i],s[j])