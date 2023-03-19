t = int(input())
while t > 0:
    a, b, c, d, x = map(int, input().split())
    g = a/c
    h = b/d
    if g > h:
        if h >= x:
            print("YES")
        else:
            print("NO")
    else:
        if g >= x:
            print("YES")
        else:
            print("NO")
    t -= 1
