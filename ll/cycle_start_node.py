# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            #this condisition if before will return first node as start (since at that slow==head)
            if slow==fast:
                slow = head
                while slow!=fast:
                    slow = slow.next
                    fast = fast.next
                
                return slow

        return None