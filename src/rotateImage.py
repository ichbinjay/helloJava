n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n-1, -1, -1):
        print(arr[j][i], end=" ")
    print()
    