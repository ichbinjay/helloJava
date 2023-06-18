from typing import List


class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        previous = set()
        def generatePermutations(nums):
            def helper(nums, path):
                if not nums:
                    res.append(path)
                    return
                for i in range(len(nums)):
                    helper(nums[:i] + nums[i+1:], path + [nums[i]])
            res = []
            helper(nums, [])
            return res
        

        def isSpecial(p):
            for i in range(len(p) - 1):
                if p[i] % p[i+1] == 0 and (p[i], p[i+1]) not in previous:
                    previous.add((p[i], p[i+1]))
                    return True
                elif p[i+1] % p[i] == 0 and (p[i+1], p[i]) not in previous:
                    previous.add((p[i+1], p[i]))
                    return True
            return False
        
        if len(nums) == 1:
            return 1
        if len(nums) == 2:
            if nums[0] % nums[1] == 0 or nums[1] % nums[0] == 0:
                return 2
            else:
                return 0
            

        count = 0
        perms = generatePermutations(nums)
        print(perms)
        for permutation in perms:
            if isSpecial(permutation):
                count += 1
        return count
    
s = Solution()
print(s.specialPerm([31, 93]))
print(s.specialPerm([2, 3, 6]))
print(s.specialPerm([1, 3, 4]))