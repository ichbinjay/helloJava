t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    for i in range(n):
        if arr[i] <= 0 and arr[i] > n:
            arr[i] = n+10
    
    for i in range(n): 
        if(abs(arr[i])!=n+10):
            arr[abs(arr[i])-1] = -abs(arr[abs(arr[i])-1])

    for i in range(n):
        if arr[i] > 0:
            print(i+1)
            break
    else:
        print(n+1)
        