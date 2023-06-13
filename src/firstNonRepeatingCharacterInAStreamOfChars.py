import collections
class Solution:
    def solve(self, s):
        res = ""
        q = collections.deque()
        count = [0 for x in range(26)]
        for i in range(len(s)):
            q.append(s[i])
            count[ord(s[i])-ord('a')]+=1
            while q:
                if count[ord(q[0])-ord('a')] > 1:
                    q.popleft()
                else:
                    res+=q[0]
                    break

            if not q:
                res+="#"
        return res