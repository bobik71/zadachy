a, b = map(int, input().split())
h1, m1 = map(int, input().split())
h2, m2 = map(int, input().split())
mh = a * b
mh1 = (b * h2) + m2
mh2 = (b * h1) + m1
mh3 = mh1 - mh2
print(mh3+1)
