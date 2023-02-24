n = list(input())
sum = sum([int(i)**3 for i in n])
if sum == int(''.join(n)):
    print('Yes')
else:
    print('No')