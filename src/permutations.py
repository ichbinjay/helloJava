from typing import List


class Solution:
    res = []
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.helper(nums, [])
        return self.res

    def helper(self, nums, path):
        if not nums:
            self.res.append(path)
            return
        for i in range(len(nums)):
            self.helper(nums[:i] + nums[i+1:], path + [nums[i]])


s = Solution()
print(s.permute([2, 3, 6]))

# other
def permuteUnique(nums):
    nums.sort()  # Sort the array to handle duplicates efficiently
    result = []
    visited = [False] * len(nums)

    def backtrack(curr_perm, visited, depth):
        if depth == len(nums):
            result.append(curr_perm)
            return

        for i in range(len(nums)):
            if visited[i]:
                continue

            if i > 0 and nums[i] == nums[i-1] and not visited[i-1]:
                continue

            visited[i] = True
            backtrack(curr_perm + [nums[i]], visited, depth + 1)
            visited[i] = False

    backtrack([], visited, 0)
    return result

# Read input
N = int(input())
nums = list(map(int, input().split()))

# Call the function and print the result
permutations = permuteUnique(nums)
for perm in permutations:
    print(*perm)