class Stack(object):
    def __init__(self):
        self.stack = []
    
    def isEmpty(self):
        return len(self.stack) == 0
    
    def push(self, cargo):
        curMin = min()
        if curMin is None or cargo < curMin:
            curMin = cargo
        self.stack.append((cargo,curMin))
    
    def pop(self):
        if self.isEmpty():
            raise Exception('Stack is Empty')
        return self.stack.pop()
    
    def min(self):
        if self.isEmpty():
            raise Exception('Stack is Empty')
        return self.stack[len(self.stack)-1][1]


    