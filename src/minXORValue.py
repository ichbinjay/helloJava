class Solution:
	# @param A : list of integers
	# @return an integer
	def findMinXor(self, arr):
        arr = sorted(arr)
        min_xor = arr[0] ^ arr[1]
        for i in range(1, len(arr) - 1):
            min_xor = min(min_xor, arr[i] ^ arr[i + 1])
        return min_xor