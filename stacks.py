class Stack:
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return self.stack == []

    def push(self,data):
        self.stack.append(data)
        
    def pop(self):
        data = self.stack[-1]
        del self.stack[-1]
        return data

    def peek(self):
        data = self.stack[-1]
        return data
    def sizeStack(self):
        return len(self.stack)
        

stack = Stack()
stack.push(1)
stack.push(4)
stack.push(33)
stack.push(77)
print(stack.sizeStack())
print(stack.pop())
print(stack.peek())
print(stack.sizeStack())

