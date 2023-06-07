'''
Problem Description
 
 

Given an even number ( greater than 2 ), return two prime numbers whose sum will be equal to the given number.
If there is more than one solution possible, return the lexicographically smaller solution i.e.
If [a, b] is one solution with a <= b,
and [c,d] is another solution with c <= d, then

[a, b] < [c, d] 
If a < c OR ( a == c AND b < d ).
NOTE: A solution will always exist. read Goldbach's conjecture


Problem Constraints
1 <= A <= 2 * 107


Input Format
The first argument is an integer A.


Output Format
Return an array of integers.


Example Input
4


Example Output
[2, 2]


Example Explanation
2 + 2 equals 4, which is the lexicographically smaller solution

'''

class Solution:
	# @param A : integer
	# @return a list of integers
    def primesum(self, A):
        if A <= 2:
            return []
        primes = [True] * A
        primes[0] = primes[1] = False
        for i in range(2, int(A ** 0.5) + 1):
            if primes[i]:
                primes[i * i:A:i] = [False] * len(primes[i * i:A:i])
        for i in range(2, A):
            if primes[i] and primes[A - i]:
                return [i, A - i]
        return []
