t = int(input())
for _ in range(t):
    n, q = map(int, input().split())
    arr = [0 for _ in range(n)]
    for _ in range(q):
        k, i = map(int, input().split())
        if k == 1:
            arr[i] ^= 1
        else:
            left = -1
            right = n
            for j in range(i-1, -1, -1):
                if arr[j] == 1:
                    left = j
                    break
            for j in range(i+1, n):
                if arr[j] == 1:
                    right = j
                    break

            if left == -1 and right == n:
                print(-1)
            elif right == n:
                print(i-left)
            elif left == -1:
                print(right-i)
            else:
                print(min(right-i, i-left))


