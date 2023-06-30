from collections import defaultdict


n, k = map(int, input().split())
#create defaultdict with default value of 0
d = defaultdict(int)
strs = input().split()
for s in strs:
    d[s] += 1
#sort by frequency, then by lexicographical order
sorted_d = sorted(d.items(), key=lambda x: (-x[1], x[0]))
for i in range(k):
    print(sorted_d[i][0])
    
