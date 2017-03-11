class Queue(object):

    def __init__(self):
        self.inStack,self.outStack = [],[]
    
    def push(self,cargo):
        self.inStack.append(cargo)
    
    def Move(self):
        while len(self.inStack) != 0:
            self.outStack.append(self.inStack.pop())
    
    def pop(self):
        self.Move()
        if len(self.outStack) == 0:
            raise Exception('Queue is empty')
        return self.outStack.pop()
    
    def peek(self):
        self.Move()
        if len(self.outStack) == 0:
            raise Exception('Queue is Empty')
        return self.outStack[-1]


q = Queue()
q.push(1)
q.push(2)
q.push(3)
print q.peek()
print q.pop()