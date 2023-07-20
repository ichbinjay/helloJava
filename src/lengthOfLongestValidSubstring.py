class Solution:
    def generateSusbtrings(self, word: str) -> List[str]:
        substrs = []
        for i in range(len(word)):
            for j in range(i+1, len(word)+1):
                substrs.append(word[i:j])
        return substrs

    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        subsstrs = self.generateSusbtrings(word)
        longestValidLen = 0
        for substr in subsstrs:
            for forb in forbidden:
                if forb in substr:
                    break
            else:
                longestValidLen = max(longestValidLen, len(substr))

        return longestValidLen
    

class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        length = 0
        all = set()
        for s in forbidden:
            all.add(s)
            length = max(length, len(s))
        n = len(word)
        r = 0
        right = n
        for i in range(n - 1, -1, -1):
            if right <= r:
                break
            temp = ''
            for j in range(i, min(right, i + length)):
                temp += word[j]
                if temp in all:
                    right = j
                    break
            r = max(r, right - i)
        return r