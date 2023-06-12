class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return "Empty"

    def is_empty(self):
        return len(self.stack) == 0


# Driver code
t = int(input())
stack = Stack()

for _ in range(t):
    operation = input().split()
    if operation[0] == "push":
        stack.push(int(operation[1]))
    elif operation[0] == "pop":
        print(stack.pop())
