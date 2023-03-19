def interleavings(A, B):
    if not A:
        return [B]
    if not B:
        return [A]
    
    res = []
    
    # Take the first character from A
    for s in interleavings(A[1:], B):
        res.append(A[0] + s)
    
    # Take the first character from B
    for s in interleavings(A, B[1:]):
        res.append(B[0] + s)
        
    return res
    
t = int(input())

for i in range(t):
    A, B = input().split()
    inter = interleavings(A, B)
    inter.sort()
    print("Case #{}:".format(i+1))
    for s in inter:
        print(s)
