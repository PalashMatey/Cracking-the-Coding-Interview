def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        try:
            slow = head
            fast = head.next
            while slow is not fast:
                slow = slow.next
                fast = fast.next.next
                
        except:
            return None
        
        slow = slow.next
        while head is not slow:
            head = head.next
            slow = slow.next
        return head