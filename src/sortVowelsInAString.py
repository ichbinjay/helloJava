from collections import defaultdict


class Solution:
    def __init__(self) -> None:
        vowels = defaultdict(int)
        vowels['a'] = 1
        vowels['e'] = 2
        vowels['i'] = 3
        vowels['o'] = 4
        vowels['u'] = 5
        vowels['A'] = 1
        vowels['E'] = 2
        vowels['I'] = 3
        vowels['O'] = 4
        vowels['U'] = 5
        self.vowels = vowels


    def isVowel(self, c: str) -> bool:
        return bool(self.vowels[c])

    def sortVowels(self, s: str) -> str:
        res = ''
        vowelstr = ''
        for i in s:
            if self.isVowel(i):
                vowelstr+=i
        vowelstr = sorted(vowelstr)

        for i in s:
            if self.isVowel(i):
                res+=vowelstr.pop(0)
            else:
                res+=i
        return res
        
        