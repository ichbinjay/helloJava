a = [1,2,3]
m = 3
for i in range(m-1,0,-1):
    a[i] = a[i-1]
print(a)