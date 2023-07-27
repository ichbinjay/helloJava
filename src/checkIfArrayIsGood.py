import collections


class Solution:
    def isGood(self, arr: List[int]) -> bool:
        length = 0
        maxElem = -1
        occurences = collections.defaultdict(int)
        for i in arr:
            length+=1
            maxElem = max(i, maxElem)
            occurences[i]+=1

        return length == maxElem + 1 and \
                occurences[maxElem]==2
        