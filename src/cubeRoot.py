# finds cube root of a number, number is guaranteed to be perfect cube

import sys

def valid(cbrt, n):
    return cbrt ** 3 <= n

def cube_root(n):
    if n == 0:
        return 0
    l, r = 1, abs(n)
    if n < 0:
        l, r = -abs(n), -1
    while l <= r:
        mid = (l + r) // 2
        if valid(mid, n):
            l = mid + 1
        else:
            r = mid - 1
    cbrt = l - 1
    if n < 0:
        cbrt = -cbrt    
    return cbrt

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        if n < 0:
            print(-1*cube_root(n))
        else:
            print(cube_root(n))
