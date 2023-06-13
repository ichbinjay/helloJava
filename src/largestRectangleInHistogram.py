from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                ind, height = stack.pop()
                maxArea = max(maxArea, (i-ind)*height)
                start = ind
                '''
                there is problem I ran into. how do I keep track of the point
                from where that particular area began? like, if we had 6 in stack 
                and new addition was 5, then we will pop. the area, however, will be
                5 units from the 6 and 5 units from the 5th one. how do we know that 
                there are 5 units from the the 6th block also. this is where the start 
                variable comes into play. using this variable, we can keep track of the
                earliest(i.e, the first block from which it got an area) block.
                '''
            stack.append((start,h))


        '''
        after completing above portion, our stack will be a monotonically decreasing stack
        or just an empty stack. the below for loop is used to deal with the case of a non
        empty stack.  
        '''
        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        return maxArea