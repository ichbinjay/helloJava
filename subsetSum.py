def func(n):
    dp = [0 for i in range(6)]
    dp[0] = 1
    for i in range(1, n+1):
        sum = 0
        for j in range(1, 7):
            if i - j >= 0:
                sum += dp[(i-j)%6]
        dp[i%6] = sum
    print(dp[n%6]%((10**9)+7))

def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        func(n)

main()