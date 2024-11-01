# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# p.next=cur.next
# cur.next=cur.next.next
# 1->2->3->4
# h->2->1->3->4
# h->2
# temp=2
# 1->3
# 2->1
# 2->1->4->3->NOne
# 
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return None
        cur = head
        #newHead would be next node, example 1->2->3->4, 2 will new head
        prev, newHead = None, head.next
        while cur:
            if cur.next:
                #4 is adj node and 3 is cur node
                adjacent_node = cur.next
                #if prev is there,lets say cur node is 3, prev would be 1(after swap), so prev.next should be 4(cur.next, aka adjacent_node)
                if prev:
                    prev.next = adjacent_node
                #3.next should be what adjecetn node.next is that is None, and adjcent_node(4) should point to 3
                cur.next, adjacent_node.next = adjacent_node.next, cur
            prev=cur
            cur=cur.next
        
        return newHead if newHead else head
