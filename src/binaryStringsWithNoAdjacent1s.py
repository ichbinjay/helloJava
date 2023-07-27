def resFunc(n):
    zeroend = 1
    oneend = 1
    if n==1:
        return 2
    else:
        exp = 1000000007
        ttl = zeroend+oneend
        for _ in range(2, n+1):
            oneend = zeroend%exp
            zeroend = ttl%exp
            ttl = zeroend+oneend%exp
        return ttl%exp


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        print(resFunc(n))


main()