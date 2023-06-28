'''
You are given an array representing a row of seats where seats[i] = 1 represents a person sitting in the ith seat, and seats[i] = 0 represents that the ith seat is empty (0-indexed).

There is at least one empty seat, and at least one person sitting.

Alex wants to sit in the seat such that the distance between him and the closest person to him is maximized.

Return that maximum distance to the closest person.

Input Format

The First line contains a integer N denoting the size of array.
The Second line contains N integers denoting the elements of array.
Constraints

2 <= seats.length <= 2 * 10^4
seats[i] is 0 or 1.
At least one seat is empty.
At least one seat is occupied.
Output Format

Print a integer which is the answer to the question.

Sample Input 0

3
0 1 0 
Sample Output 0

1
Sample Input 1

4
1 0 0 0
Sample Output 1

3
'''
# Solution
class Solution(object):
    def maxDistToClosest(self, seats):
        n = len(seats)
        left = [n] * n
        right = [n] * n

        for i in range(n):
            if seats[i] == 1:
                left[i] = 0
            elif i > 0:
                left[i] = left[i-1] + 1

        for i in range(n-1, -1, -1):
            if seats[i] == 1:
                right[i] = 0
            elif i < n-1:
                right[i] = right[i+1] + 1

        return max(min(left[i], right[i]) for i in range(n) if not seats[i])