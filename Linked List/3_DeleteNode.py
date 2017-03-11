#Given the node that must be deleted, we must delete the node. 

class ListNode(object):
    def __init__(self,x):
        self.data = x
        self.next = None

class LinkedList(object):
    def __init__(self):
        self.head = None

    def add(self,data):
        node = ListNode(data)

        if self.head == None:
            self.head = node
        else:
            node.next = self.head
            self.head = node
    
    def getData(self):
        return self.getData
    
    def getNext(self):
        return self.next
    
    def setData(self,newData):
        self.data = newData

    def print_linkedList(self):
        temp = self.head
        while(temp):
            print temp.data,
            temp = temp.next
        
    def deleteNode(self, node):
        if node is None or node.next is None:
            return False
        node.data = node.next.data
        node.next = node.next.next

    def printNode(self,node):
        if node:
            print '\n',node.data

    def getMiddleNode(self):
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        self.printNode(fast) 
    
    def getRangeofFast(self):
        slow = fast = self.head
        for _ in range(2):
            fast = fast.next
            self.printNode(fast)
        while fast.next:
            slow = slow.next
            fast = fast.next
        self.printNode(fast)

    def deleteNodeN(self, n):
        i = 1
        x = self.head
        while x and i != n:
            x = x.next
            i += 1
        self.deleteNode(x)

ll = LinkedList()
ll.add(1)
ll.add(2)
ll.add(3)
ll.add(4)
ll.add(3)
ll.add(2)
ll.add(1)

ll.print_linkedList()
ll.getMiddleNode

# ans = ll.deleteNodeN(4)
# print '\nAfter deleting the node: ',
# ll.print_linkedList()