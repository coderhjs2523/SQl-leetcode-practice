class MinStack(object):

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, value):
        self.stack.append(value)

        if not self.min_stack or value <= self.min_stack[-1]:
            self.min_stack.append(value)
        

    def pop(self):
        pop_value = self.stack.pop()

        if pop_value == self.min_stack[-1]:
            self.min_stack.pop()
        

    def top(self):
       return self.stack[-1]
        

    def getMin(self):
        return self.min_stack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()