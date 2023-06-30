n = int(input())
arr = [0 for i in range(n)]
inp = [int(i) for i in input().split()]
for i in range(n):
    arr[inp[i]-1] = 1

for i in range(n):
    if arr[i] == 0:
        print(i+1, end=' ')
        

