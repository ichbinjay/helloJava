def check_triplets(arr, n, k):
    arr.sort()
    for i in range(n-2):
        left = i+1
        right = n-1
        while left < right:
            if arr[i] + arr[left] + arr[right] == k:
                return True
            elif arr[i] + arr[left] + arr[right] < k:
                left += 1
            else:
                right -= 1
    return False

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    if check_triplets(arr, n, k):
        print("true")
    else:
        print("false")
