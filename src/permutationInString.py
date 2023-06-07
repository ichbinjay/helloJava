class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        windowSize = len(s1)
        for i in range(len(s2)-windowSize+1):
            if sorted(s2[i:i+windowSize]) == sorted(s1): return True


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        windowSize = len(s1)
        hm1 = {chr(i):0 for i in range(97,123)}
        for c in s1: hm1[c] += 1
        for i in range(len(s2)-windowSize+1):
            hm2 = {chr(i):0 for i in range(97,123)}
            for c in s2[i:i+windowSize]: hm2[c] += 1
            if hm1 == hm2: return True