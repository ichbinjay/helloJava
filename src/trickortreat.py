'''
Halloween is around and Ted Mosby ( who loves kids ) wants to give away candies. Ted has N bags of candies, each bag has Candies equal to A[i] stored in an array A[N]. There are M kids and each kid wants a specific amount of candy C[i] stored in an array C[M].

For every kid i, you are to print "Happy Halloween!" if C[i] is present in the array A[N]. If C[i] is not present in the array, print "Tricky!".

Hint1 : You can use binary search to find out whether an element is present in the array or not.

INPUT

First line contains the number N(1 <= N <= 10^5), size of array A[N]. Second line contains N space separated integers, denoting the elements of the array A. (1 <= A[i] <= 10^9) Third line contains the number M(1 <= M <= 10^5), size of array C[M]. Fourth line contains M space separated integers, denoting the elements of the array C. (1 <= C[i] <= 10^9)

OUTPUT

Print M lines of output. ith line being "Happy Halloween!" if C[i] is present in A[N] and "Tricky!" otherwise.
'''

def binary_search(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, high, x)
    else:
        return -1

n = int(input())
a = list(map(int, input().split()))
m = int(input())
c = list(map(int, input().split()))
a.sort()s
for i in range(m):
    if binary_search(a, 0, n - 1, c[i]) != -1:
        print("Happy Halloween!")
    else:
        print("Tricky!")