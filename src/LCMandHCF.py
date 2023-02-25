t = int(input())
for _ in range(t):
    a, b = map(int,input().split())
    x, y = max(a, b), min(a, b)
    while y > 0:
        x, y = y, x % y
    hcf = x

    # Calculate LCM
    lcm = (a * b) // hcf
    print(lcm, hcf, sep=" ")
