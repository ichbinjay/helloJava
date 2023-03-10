def power(a, b):
    result = 1
    mod = 1000000007
    while b > 0:
        if b & 1 == 1:
            result = (result * a) % mod
        a = (a * a) % mod
        b >>= 1
    return result % mod

t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    print(power(a, b))
