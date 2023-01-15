s = "aaa"
l, r = 0, 0

count = 0
while r < len(s):
    if s[l:r + 1] == s[l:r + 1][::-1]:
        count += 1
    r += 1
    if r == len(s):
        l += 1
        r = l
print(count)