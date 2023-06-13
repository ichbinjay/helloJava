class Solution:
	# @param A : tuple of integers
	# @param B : integer
	# @return a list of integers
	def slidingMaximum(self, A, B):
        sums = []
        for i in range(0, len(A)-B+1):
            sums.append(max(A[i:i+B]))
        return sums


class Solution:
    def slidingMaximum(self, nums, k):
        from collections import deque
        q = deque()
        res = []
        l , r = 0, 0
        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            if l > q[0]:
                q.popleft()

            if (r+1)>=k:
                res.append(nums[q[0]])
                l+=1
            r+=1

        return res

		