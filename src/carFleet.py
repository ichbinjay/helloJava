from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[p, s] for p, s in zip(position, speed)]
        stack = []
        for p, s in sorted(pair):
            eta = (target - p) / s
            if not stack:
                stack.append(eta)
            else:
                while stack and eta >= stack[-1]:
                    stack.pop()
                stack.append(eta)
        return len(stack)

sol = Solution()
print(sol.carFleet(12, [10,8,0,5,3], [2,4,1,1,3]))
