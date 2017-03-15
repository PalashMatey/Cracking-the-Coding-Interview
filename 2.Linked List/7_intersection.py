def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        lenA = 0
        lenB = 0
        pa,pb = headA, headB
        while pa:
            lenA += 1
            pa = pa.next
        while pb:
            lenB += 1
            pb = pb.next
        curA,curB = headA,headB
        if lenA > lenB:
            for i in range(lenA - lenB):
                curA = curA.next
        else:
            for i in range(lenB - lenA):
                curB = curB.next
        while curA is not curB:
            curA = curA.next
            curB = curB.next
        return curA