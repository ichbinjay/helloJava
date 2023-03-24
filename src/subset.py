class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def subsets(self, A):
        limit = 2 ** len(A)
        A.sort()
        result = []
        for i in range(limit):
            temp = []
            for j in range(len(A)):
                if i & (1 << j):
                    temp.append(A[j])
            result.append(temp)
        result.sort()
        return result

s = Solution()
print(s.subsets([1,2,3]))
print(s.subsets([12,13]))