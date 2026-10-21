class MyQueue(object):

    def __init__(self):
        self.stack = []

    def push(self, x):
        temp = []

        while self.stack:
            temp.append(self.stack.pop())

        self.stack.append(x)

        while temp:
            self.stack.append(temp.pop())
        
    def pop(self):
        return self.stack.pop()
        
    def peek(self):
        return self.stack[-1]
        
    def empty(self):
        return len(self.stack) == 0
        

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()