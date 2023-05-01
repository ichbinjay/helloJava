class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        reslen = 1
        n = len(s)
        if n == 0:
            return 0
        l,r = 0, 1
        while l < n and r < n and l < r: 
            if len(s[l:r+1]) == len(set(list(s[l:r+1]))):
                if len(s[l:r+1]) > reslen:
                    reslen = len(s[l:r+1])
                r+=1
            else:
                l+=1

            if l==r:
                r+=1
        return reslen
