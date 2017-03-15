#from LinkedList import LinkedList

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
        
    def partition(self,val):
        current = self.head
        prev = None
        while current:
            if prev and current.data < val:
                prev.next = current.next
                current.next = self.head
                self.head = current
                current = prev.next
            else:
                prev = current
                current = current.next
