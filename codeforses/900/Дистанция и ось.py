t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    
    if k == 0:
        print(0)
        continue
    
    # Находим ближайшее A' >= k, A' ≡ k (mod 2)
    target = k if (k % 2 == n % 2) else k + 1
    steps = max(0, target - n)
    
    print(steps)

