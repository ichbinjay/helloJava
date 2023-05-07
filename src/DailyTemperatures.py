from typing import List


class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        res = [0] * len(temps)
        stack = []
        for i, t in enumerate(temps):
            while stack and temps[i] > stack[-1][0]:
                popped_temp, popped_index = stack.pop()
                res[popped_index] = i - popped_index
            stack.append((t, i))
        return res

sol = Solution()
print(sol.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))