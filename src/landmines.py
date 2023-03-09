from collections import deque

m, n = map(int, input().split())
a = []
for i in range(m):
    a.append(list(input().split()))

deq = deque()
res = []
for i in range(m):
    row = []
    for j in range(n):
        if a[i][j] == 'M':
            deq.append((i, j, 0))
            row.append(0)
        elif a[i][j] == 'X':
            row.append("NULL")
        else:
            row.append(-1)
    res.append(row)

while deq:
    i, j, d = deq.popleft()
    for ni, nj in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
        if 0 <= ni < m and 0 <= nj < n and res[ni][nj] == -1:
            res[ni][nj] = d+1
            deq.append((ni, nj, d+1))

for i in range(m):
    for j in range(n):
        if res[i][j] == "NULL":
            print("-1", end=" ")
        else:
            print(res[i][j], end=" ")
    print()

