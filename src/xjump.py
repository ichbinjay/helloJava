t = int(input())
for _ in range(t):
    x, y = map(int,input().split())
    steps = 0
    while x > y:
        x -= y
        steps += 1
    while x > 0:
        x -= 1
        steps += 1
    print(steps)