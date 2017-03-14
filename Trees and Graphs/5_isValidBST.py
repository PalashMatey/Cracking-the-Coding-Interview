def isValidBST(self, root , minl = float('-inf'), maxh = float('inf') ):
    """
    :type root: TreeNode
    :rtype: bool
    """
    if not root:
        return True
        
    if root.val <= minl or root.val >= maxh:
        return False
    
    return self.isValidBST(root.left, min(minl,root.val), root.val) and self.isValidBST(root.right, root.val, max(maxh,root.val))