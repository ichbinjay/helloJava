def find_number(X, Y):
    number = 0
    res1 = (1 << X)
    res2 = (1 << Y)
    number |= res1
    number |= res2
    return number

t = int(input())
for i in range(t):
    X, Y = map(int, input().split())
    print(find_number(X, Y))
