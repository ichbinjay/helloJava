# Given a number, check if it is a power of 2.
t = int(input())
for i in range(t):
    n = int(input())
    if n & (n-1) == 0:
        print("True")
    else:
        print("False")