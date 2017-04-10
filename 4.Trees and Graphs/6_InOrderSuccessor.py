class Node:

    def __init__(self,data):
        self.data = data
        self.right = right
        self.left = left

def inOrderSuccessor(root,n):
    #Step 1: Check if the right subtree is not None, and return rightmost value
    if n.right is not None:
        return minValue(n.right)
    
    #Step 2: If right subtree is empty then inorder successor is the parent of current node
    p = n.parent
    while p is not None:
        if n != p.right:
            break
        n = p
        p = p.parent
    return p


def minValue(node):
    current = node

# loop down to find the leftmost leaf
while(current is not None):
    if current.left is None:
        break
    current = current.data

return current

def insert( node, data):
     
    # 1) If tree is empty then return a new singly node
    if node is None:
        return Node(data)
    else:
        
        # 2) Otherwise, recur down the tree
        if data <= node.data:
            temp = insert(node.left, data)
            node.left = temp 
            temp.parent = node
        else:
            temp = insert(node.right, data)
            node.right = temp 
            temp.parent = node
         
        # return  the unchanged node pointer
        return node
 