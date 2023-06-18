t= int(input())
for i in range(t):
    n,d = map(int,input().split())
    d = d%n
    arr = list(map(int,input().split()))
    arr.reverse()
    arr1 = arr[:d]
    arr1.reverse()
    arr2 = arr[d:]
    arr2.reverse()
    print(*arr1,*arr2,sep=" ")