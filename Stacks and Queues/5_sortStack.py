class Node(object):
    def __init__(self,data,next = None):
        self.data = data
        self.next = next
    
class Stack(object):
    def __init__(self,top = None):
        self.top = top
    
    def push(self,data):
        self.top = Node(data,self.top)
    
    def pop(self):
        if self.top is None:
            raise Exception('Stack is Full')
        value = self.top.data
        self.top = self.top.next
        return value
    
    def peek(self):
        if self.top is None:
            raise Exception('Stack is Empty')
        return self.top.data
    
    def isEmpty(self):
        return self.top == None
    
    def copy(self):
        s = Stack()
        cur = self.top
        while cur:
            s.push(cur.data)
            cur = cur.next
        return s
    
    def printStack(self):
        cur = self.top
        while cur:
            print cur.data,
            cur = cur.next
        
    
def sortStack(st):
    s = st.copy()
    r = Stack()
    while not s.isEmpty():
        temp = s.pop()
        while not r.isEmpty() and temp > r.peek():
            s.push(r.pop())
        r.push(temp)
    return r
s = Stack()
s.push(-5)
s.push(-1)
s.push(20)
s.push(10)
r = sortStack(s)
r.printStack()
print r.peek()