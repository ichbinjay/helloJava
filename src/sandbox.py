s = "AABA"
k = 1

count = {}
res = 0

l = 0
maxf = 0
for r in range(len(s)):
    count[s[r]] = count.get(s[r], 0) + 1
    maxf = max(maxf, count[s[r]])
    if r - l + 1 - maxf > k:
        count[s[l]] -= 1
        l += 1
    res = max(res, r - l + 1)
return res