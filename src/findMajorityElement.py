n = input()# k = floor(n/2)
k = int(n)//2
arr = list(map(int,input().split()))
ht = {}
for i in arr:
    if i in ht:
        ht[i] += 1
    else:
        ht[i] = 1
for i in ht:
    if ht[i] >= k:
        print(i)
        break
