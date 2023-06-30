n,k=map(int,input().split())
a=list(map(int,input().split()))
m=max(a)
for i in a:
    if i+k>=m:print('true',end=' ')
    else: print('false',end=' ')
