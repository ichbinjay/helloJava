class MinStack(object):
    def __init__(self):
        self.stack = list()
        self.minstack = list()

    def push(self, val):
        self.stack.append(val)
        
        if self.minstack:
            if self.minstack[-1] < val:
                self.minstack.append(self.minstack[-1])
            else:
                self.minstack.append(val)
        else:
            self.minstack.append(val)

    def pop(self):
        del self.stack[-1]
        del self.minstack[-1]
        

    def top(self):
        return self.stack[-1]
        

    def getMin(self):
        return self.minstack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()