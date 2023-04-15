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
