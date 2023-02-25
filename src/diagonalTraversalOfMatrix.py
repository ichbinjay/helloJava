t = int(input())
for _ in range(t):
    n = int(input())
    a = []
    for i in range(n):
        a.append(list(map(int,input().split())))
    indices = [x for x in range(-n+1, n)]

    for k in indices:
        ttl = 0
        for i in range(n):
            for j in range(n):
                if i-k == j:
                    ttl += a[i][j]
        print(ttl, end=" ")
    print()
