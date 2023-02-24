import math
t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    for i in range(a, b+1):
        flag = False
        for j in range(2, int(math.sqrt(i))+1):
            if i % j == 0:
                flag = True
                break
        if not flag and i != 1:
            print(i)
    print()
