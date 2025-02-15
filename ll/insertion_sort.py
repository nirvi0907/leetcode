# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        start = ListNode(float(-inf), None)
        start.next = head
        prev = head
        cur = head.next
        
        while cur:
            # print(cur)
            if cur.val>=prev.val:
                prev, cur = cur, cur.next
                continue
            iterator = start
            while iterator.next.val<cur.val:
                iterator = iterator.next 
            
            nxt = cur.next #3
            prev.next = nxt #
            cur.next = iterator.next #2->4
            iterator.next = cur
            # prev = cur#2
            cur = nxt#1
            # print(start)
            # break
        return start.next
