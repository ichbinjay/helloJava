class Solution:
    def maxScore(self, nums: List[int], x: int) -> int:
        evenCount, oddCount = 0, 0
        evenSum, oddSum = 0, 0
        evenElem, oddElem = [], []
        res = 0
        for i in range(len(nums)):
            if i%2==0:
                evenCount+=1
                evenSum+=nums[i]
            else:
                oddCount+=1
                oddSum+=nums[i]

        if evenCount> oddCount:
            res = evenSum
            mx = max(oddElem)
            while mx > x:
                res += mx
                oddElem.remove(mx)
                mx = max(oddElem)
        elif oddCount > evenCount:
            res = oddSum
            mx = max(evenElem)
            while mx > x:
                res += mx
                evenElem.remove(mx)
                mx = max(evenElem)
        else:
            res = max(evenSum, oddSum)
            mx = max(evenElem)
            while mx > x:
                res += mx
                evenElem.remove(mx)
                mx = max(evenElem)
            mx = max(oddElem)
            while mx > x:
                res += mx
                oddElem.remove(mx)
                mx = max(oddElem)
        return res
    


            