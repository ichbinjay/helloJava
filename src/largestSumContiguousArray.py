# Python program to find maximum contiguous subarray

# Function to find the maximum contiguous subarray
from sys import maxsize


def maxSubArraySum(a, size):

	max_so_far = -maxsize - 1
	max_ending_here = 0

	for i in range(0, size):
		max_ending_here = max_ending_here + a[i]
		if (max_so_far < max_ending_here):
			max_so_far = max_ending_here

		if max_ending_here < 0:
			max_ending_here = 0
	return max_so_far

# Driver function to check the above function


n = int(input())
a = list(map(int, input().split()))
print(maxSubArraySum(a, n))

# This code is contributed by _Devesh Agrawal_
