class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        string =""
        result =[]
        for d in digits:
            string += str(d)
        i = int(string) + 1
        for w in str(i):
            result.append(w)
        return [int(x) for x in result]