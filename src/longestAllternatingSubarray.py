from typing import List


class Solution:
    def genreateSubarrays(self, nums):
        subarrs = []
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                subarrs.append(nums[i:j + 1])
        return subarrs

    def isAlt(self, arr):
        for i in range(len(arr) - 1):
            if i%2==0:
                if arr[i+1]-arr[i] != 1:
                    return False
            else:
                if arr[i+1]-arr[i] != -1:
                    return False
        return True

    def alternatingSubarray(self, nums: List[int]) -> int:
        subarrs = self.genreateSubarrays(nums)
        subarrs = [subarr for subarr in subarrs if len(subarr) > 1]

        altCount = -1
        for subarr in subarrs:
            if self.isAlt(subarr):
                altCount = max(altCount, len(subarr))

        return altCount


s = Solution()
print(s.alternatingSubarray([2,3,4,3,4]))
print(s.alternatingSubarray([4, 5, 6]))
