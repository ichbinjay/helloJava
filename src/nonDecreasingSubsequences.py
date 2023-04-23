# bitmanipulation solution
import sys

def solve(arr, size):
    count = 0
    for i in range(1<<size):
        if(isValid(arr, size, i)):
            count += 1
    return count


def isValid(arr, size, mask):
    prev = -sys.maxsize - 1
    for i in range(size):
        if(mask & (1<<i)):
            if(arr[i] < prev):
                return False
            prev = arr[i]
    return True


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().strip().split()))
    res = solve(a, n)
    print(res-1)

# recursive solution
def solve(arr, size, ind, prev):
    if ind == size:
        return 1
    count = 0
    if arr[ind] >= prev:
        count += solve(arr, size, ind+1, arr[ind])
    count += solve(arr, size, ind+1, prev)
    return count


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().strip().split()))
    res = solve(a, n, 0, 0)
    print(res-1)

#dp solution
MOD = 1000000007

# recursive function to compute the number of non-decreasing subsequences ending at index i
def countSubsequences(a, dp, i):
    # if result is already computed, return it
    if dp[i] != -1:
        return dp[i]
    
    # initialize result to 1, since a[i] itself forms a non-decreasing subsequence
    res = 1
    
    # compute the sum of the number of non-decreasing subsequences for all previous indices j such that a[j] <= a[i]
    for j in range(i):
        if a[j] <= a[i]:
            res = (res + countSubsequences(a, dp, j)) % MOD
    
    # memoize the result and return it
    dp[i] = res
    return res

# main function to read input and call the recursive function
def main():
    # read number of test cases
    t = int(input())
    
    for _ in range(t):
        # read input for each test case
        n = int(input())
        a = list(map(int, input().strip().split()))
        
        # initialize memoization array
        dp = [-1] * n
        
        # compute the total number of non-decreasing subsequences by summing up the number of non-decreasing subsequences ending at all indices
        res = 0
        for i in range(n):
            res = (res + countSubsequences(a, dp, i)) % MOD
        
        # print the result
        print(res)

# call the main function
if __name__ == '__main__':
    main()
