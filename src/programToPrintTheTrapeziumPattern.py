n = 5 # int(input())
c1 = 1
c2 = n*(n+1)
for i in range(n):
    for j in range(n):
        if i <= j:
            print("{:02d}".format(c1), end=" ")
            c1 += 1
        else:
            print("  ", end=" ")
    x = c2-n+i+1
    temp = x-1
    for j in range(n):
        if i <= j:
            print("{:02d}".format(x), end=" ")
            x += 1
    c2 = temp
    print()

'''
output:
01 02 03 04 05 26 27 28 29 30
   06 07 08 09 22 23 24 25
      10 11 12 19 20 21
         13 14 17 18
            15 16
'''