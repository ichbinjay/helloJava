'''
Given an integer N, check whether it is a Narcissistic number or not.
Note: A narcissistic number is a number that is the sum of its own digits each raised to the power of the number of digits'''
n = list(input())
sum = sum([int(i)**len(n) for i in n])
if sum == int(''.join(n)):
    print('Yes')
else:
    print('No')