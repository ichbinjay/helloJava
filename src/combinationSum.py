class Solution:
	# @param A : list of integers
	# @param B : integer
	# @return a list of list of integers
	def combinationSum(self, A, B):
        A = list(set(A))
        A.sort()
        return self.combinationSumHelper(A, B, 0, [])

    def combinationSumHelper(self, A, B, index, current):
        if B == 0:
            return [current]
        if B < 0:
            return []
        if index >= len(A):
            return []
        result = []
        for i in range(index, len(A)):
            result += self.combinationSumHelper(A, B - A[i], i, current + [A[i]])
        return result
