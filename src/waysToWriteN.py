# Given an integer n, return the number of ways you can write n as the sum of consecutive positive integers.
n = int(input())
count = 1
for i in range(1, n):
    for j in range(i, n):
        if (i+j)*(j-i+1)//2 == n:
            count += 1
print(count)

# optimal sol
n = int(input())
count = 0
i = 1
while i*(i+1)//2 <= n:
    if (n - i*(i+1)//2) % i == 0:
        count += 1
    i += 1
print(count)
