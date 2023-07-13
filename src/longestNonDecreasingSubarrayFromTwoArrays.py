def generate_lists(nums1, nums2):
    if not nums1:
        return [nums2]
    if not nums2:
        return [nums1]
    
    result = []
    for num in nums1:
        remaining = nums1.copy()
        remaining.remove(num)
        sub_lists = generate_lists(remaining, nums2)
        for sub_list in sub_lists:
            result.append([num] + sub_list)
    
    return result

class Solution:
    def maxNonDecreasingLength(self, nums1: List[int], nums2: List[int]) -> int:
        nums = []
        for i in range(len(nums1)):
            nums.append(min(nums1[i], nums2[i]))
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                return i+1
        return len(nums)
    
