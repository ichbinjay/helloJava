class Solution(object):
    def evalRPN(self, tokens):
        stack = []
        for i in tokens:
            try 
                stack.append(i)
            else:
                a = stack[-2]
                b = stack[-1]
                res = None
                if i == "+":
                    res = a+b
                elif i=="-":
                    res = a-b
                elif i=="*":
                    res = a*b
                else:
                    res = a/b
                stack[-2] = res
                del stack[-1]
        return int(stack[-1])
                