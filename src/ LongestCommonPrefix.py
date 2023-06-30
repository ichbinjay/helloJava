n = int(input())
strs = []
minLen = 300
for i in range(n):
    strs.append(input())
    minLen = min(minLen, len(strs[i]))

ans = ''
for i in range(minLen):
    c = strs[0][i]
    for j in range(n):
        if strs[j][i] != c:
            print(ans)
            exit()
    ans += c

print(ans)

