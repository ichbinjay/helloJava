'''
Given an 2 strings A and B, find the number of occurrences of A in B as a substring. Solve using Rabin-Karp string matching algorithm with multiple hash functions. Do not use inbuilt library.

Input Format

First line of input contains T - number of test cases. Its followed by T lines. Each line contains 2 strings - A and B, separated by space.

Constraints

1 <= T <= 2000
1 <= len(A), len(B) <= 10005
'a' <= A[i], B[i] <= 'z'

Output Format

For each test case, print the number of occurrences of A in B, separated by newline.

Sample Input 0

4
smart yekicmsmartplrplsmartrplplmrpsmartrpsmartwmrmsmartsmart
interviews interviewseiwcombvinterviewskrenlzp
ds dsdsajdsrjjdsjjj
algo yalgoalgoalgopalgoaxalgoasaxalgolalgoalgoalgo
Sample Output 0

6
2
4
9
'''

def rabin_karp(A, B):
    n, m = len(A), len(B)
    if n > m:
        return 0
    p, q = 31, 10**9 + 9
    p_pow = [1] * (m + 1)
    for i in range(1, m + 1):
        p_pow[i] = (p_pow[i - 1] * p) % q
    h = [0] * (m + 1)
    for i in range(1, m + 1):
        h[i] = (h[i - 1] * p + ord(B[i - 1])) % q
    h_s = 0
    for i in range(n):
        h_s = (h_s * p + ord(A[i])) % q
    count = 0
    for i in range(m - n + 1):
        if h_s == (h[i + n] - h[i] * p_pow[n]) % q:
            if A == B[i:i + n]:
                count += 1
    return count


# driver code
def main():
    T = int(input())
    for _ in range(T):
        A, B = input().split()
        print(rabin_karp(A, B))


main()
