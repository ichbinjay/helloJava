strs = ["eat","tea","tan","ate","nat","bat"]

sorted_strs = []
result_cluster = {}
for i in strs:
    srt = sorted(i)
    res = ''.join(srt)
    sorted_strs.append(res)

for i in range(len(sorted_strs)):
    if sorted_strs[i] in result_cluster:
        result_cluster[sorted_strs[i]].append(strs[i])
    else:
        result_cluster[sorted_strs[i]] = [strs[i]]
print(list(result_cluster.values()))