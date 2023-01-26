class Solution(object):
    def countSubstrings(self, s):
        count = 0
        for i in range(len(s)):
            l = r = i
            while l > -1 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
                count +=1

            l = i
            r = i+1
            while l > -1 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
                count +=1
        return count