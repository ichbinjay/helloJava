import math

class Solution(object):
    def evalRPN(self, tokens):
        stack = []
        for i in tokens:
            try:
                int(i)
                stack.append(int(i))
            except ValueError:
                a = stack[-2]
                b = stack[-1]
                res = None
                if i == "+":
                    res = a + b
                elif i == "-":
                    res = a - b
                elif i == "*":
                    res = a *  b
                else:
                    res = math.trunc(a / b)
                del stack[-2:]
                stack.append(res)
        return int(stack[-1])


sol = Solution()
print(sol.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))