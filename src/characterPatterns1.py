t = int(input())

for _ in range(t):
    l, c = map(int, input().split())

    for i in range(l):
        for j in range(c):
            if (i+j) % 2 == 0:
                print('*', end='')
            else:
                print('.', end='')
        print()

    if _ != t-1:
        print()