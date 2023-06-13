class MinStack:
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
        if self.stack and self.minstack:
            del self.stack[-1]
            del self.minstack[-1]
        

    def top(self):
        return self.stack[-1] if self.stack else -1
        

    def getMin(self):
        if self.minstack:
            return self.minstack[-1]
        else: return -1
        