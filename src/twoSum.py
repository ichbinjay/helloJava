nums = [2, 7, 11, 5]
target = 9
hm = dict()

for i, num in enumerate(nums):
    if target - num in hm:
        print([hm[target - num], i])
        break
    hm[num] = i
