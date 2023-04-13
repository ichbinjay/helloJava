class Solution(object):
    def targetIndices(self, nums, target):
        nums.sort()
        if target not in nums:
            return []
        start = nums.index(target)
        res = []
        res.append(start)
        for i in range(start+1, len(nums)):
            if nums[i]!=target:
                break
            res.append(i)
        return res
    