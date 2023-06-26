class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if len(s) == 0:
            return 0
        sign = False
        if s[0] == '-':
            sign = True
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]
        if len(s) == 0:
            return 0
        
        res =""
        for i in range(len(s)):
            if s[i].isdigit():
                res += s[i]
            else:
                break
        if len(res) == 0:
            return 0
        res = int(res)
        if sign:
            res = -res
        if res > 2**31 - 1:
            return 2**31 - 1
        if res < -2**31:
            return -2**31
        return res
