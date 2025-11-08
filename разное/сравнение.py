a = int(input())
a1 = a
s = 0
k = 0
m = 0
while a > 0:
    k = a % 10
    s = s + k
    a = a // 10
for i in range (1,a1):
    if a1 % i == 0:
        m = m + i
if s > m:
    print('сумма цифр больше')
if s < m:
    print('сумма цифр больше')
