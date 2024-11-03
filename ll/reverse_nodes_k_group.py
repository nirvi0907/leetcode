class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:        
        # Check if there are engough values to reverse
        curr = head
        for _ in range(k):
            if not curr: return head
            curr = curr.next
		        
				
        # Reverse the group (basic way to reverse linked list)
        prev = None
        curr = head
        for _ in range(k):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        print(prev.val)
        # After reverse, we know that `head` is the tail of the group.
		# And `curr` is the next pointer in original linked list order
        #head.next points to last node in next group
        head.next = self.reverseKGroup(curr, k)
        #return the last node
        return prev