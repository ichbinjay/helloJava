t = int(input())
for _ in range(t):
    n,k=map(int,input().split())
    n = [int(x) for x in input().split()]
    res = ""
    for i in n:
        if k-i >= 0:
            res+='1'
            k-=i
        else:
            res+='0'
    print(res)
