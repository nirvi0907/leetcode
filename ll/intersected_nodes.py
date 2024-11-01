# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # stackA = []
        # stackB = []
        # while headA:
        #     stackA.append(headA)
        #     headA = headA.next
        # while headB:
        #     stackB.append(headB)
        #     headB = headB.next
        # intersected_node=None
        # while stackA and stackB:
        #     nodeA = stackA.pop()
        #     nodeB = stackB.pop()

        #     if nodeA!=nodeB:
        #         return intersected_node
        #     intersected_node = nodeA
        # return intersected_node
        curA = headA
        curB = headB
        while curA:
            curA = curA.next
        while curB:
            curB=curB.next
        if curA!=curB:
            return None
        curA = headA
        curB = headB
        while curA or curB:
            if curA==curB:
                return curA
            curA = curA.next if curA else headB
            curB = curB.next if curB else headA