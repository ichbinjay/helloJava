from collections import defaultdict

t = int(input())
for _ in range(t):
    a, b = input().split()
    ctr = defaultdict(int)
    res = 0
    
    for i in range(len(a)):
        ctr[a[i]] += 1

    for i in range(len(b)):
        if b[i] in ctr:
            ctr[b[i]] -= 1
        else:
            res += 1
    res += sum([abs(x) for x in ctr.values()])
    print(res)

