s = input()
kb, ks, kc = map(int,input().split())
rb, rs, rc = map(int,input().split())
r = int(input())

nb = 0
ns = 0
nc = 0
for i in s:
    if i == 'B':
        nb += 1
    elif i == 'S':
        ns += 1
    elif i == 'C':
        nc += 1

s = 0
while kb - nb >= 0 and ks - ns >= 0 and kc - nc >= 0:
    kb -= nb
    ks -= ns
    kc -= nc
    s += 1

ob = kb-nb
os = ks-ns
oc = kc-nc

while r > 0:
    if ob < os and ob < oc and r > rb:
        kb += 1
        r -= rb
    elif os < ob and os < oc and r > rs:
        ks += 1
        r -= rs
    elif r > rc:
        kc += 1
        r -= rc
    elif rb > r and rs > r and rc > r:
        break
    ob = kb-nb
    os = ks-ns
    oc = kc-nc

while kb - nb >= 0 and ks - ns >= 0 and kc - nc >= 0:
    kb -= nb
    ks -= ns
    kc -= nc
    s += 1

print(s)