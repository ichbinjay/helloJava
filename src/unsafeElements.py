n = int(input())
m = n
a = []
for i in range(n):
    a.append(list(map(int, input().split())))

minind, maxind = [0, 0],[0, 0]
minelem, maxelem = a[0][0], a[0][0]
for i in range(n):
    for j in range(m):
        if a[i][j] > maxelem:
            maxelem = a[i][j]
            maxind = i, j
        if a[i][j] < minelem:
            minelem = a[i][j]
            minind = i, j

count = 0    
for i in range(n):
    for j in range(m):
        if not (i == maxind[0] or i == minind[0] or j == maxind[1] or j == minind[1]):
            count += 1
print(count)
