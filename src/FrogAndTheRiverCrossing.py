n = int(input())
arr = list(map(int, input().split()))
res = True
step = 0
for i in range(1, n):
    if arr[i] in [step-1, step, step+1]:
        step = arr[i]
    else:
        res = False
        break
print(res)
