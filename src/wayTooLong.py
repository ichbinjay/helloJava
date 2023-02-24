n = int(input())
for i in range(n):
    s = input()
    l = len(s)
    if l >= 11:
        print(s[0] + str(l-2) + s[l-1])
    else:
        print(s)