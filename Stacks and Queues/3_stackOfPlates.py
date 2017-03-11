class Node(object):

    def __init__(self, data, next = None):
        self.data = data
        self.next = next
    
class Stack(object):

    def __init__(self, head = None):
        self.head = head
        self.size = 0
    
    def push(self,cargo):
        self.head = Node(cargo,self.head)
        self.size += 1

    def pop(self):
        if self.isEmpty():
            raise Exception('Stack is Empty')
        cargo = self.head.data
        self.head = self.head.next
        self.size -= 1
        return cargo 

    def isEmpty(self):
        return self.size == 0
    
    def getSize(self):
        return self.size
    
    def peek(self):
        if self.isEmpty():
            raise Exception('Stack is Empty')
        else:
            return self.head.data
    
    def printStack(self):
        cur = self.head
        while cur:
            print cur.data,
            cur = cur.next
    
class SetOfStacks(object):
    
    def __init__(self,capacity):
        self.capacity = capacity
        self.stacks = [Stack()]
    
    def push(self,cargo):
        if len(self.stacks) == 0 or self.stacks[-1].getSize == self.capacity:
            self.stacks.append(Stack())
        self.stacks[-1].push(cargo)
    
    def pop(self):
        if len(self.stacks) == 0:
            raise Exception('Stack is Empty')
        cargo = self.stacks[-1].pop()
        if self.stacks[-1].getSize == 0:
            self.stacks.pop()
        return cargo
    
#shall come back to the rest of this implementation
s = SetOfStacks(10)
for i in range(101):
    s.push(i)
for i in range(101):
    print s.pop()