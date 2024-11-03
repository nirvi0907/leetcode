# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        '''
        [[]], []
        [[4,4,5],[1,3,4],[2,6]]
    q   heap=[3,2,4]
       
        r = 1,1
        [[1],[]]]
        h=[1]
        r=1
        [[1],[1,3]]
        '''
        ListNode.__eq__ = lambda self, other: self.val==other
        ListNode.__lt__ = lambda self, other:self.val<other
        heap = []
        merged_linked_list = ListNode()
        linked_list_iterator = merged_linked_list

        for index,linked_list in enumerate(lists):
            if linked_list:
                heapq.heappush(heap, (linked_list.val, linked_list))

        while heap:
            val, linked_list = heapq.heappop(heap)
            linked_list_iterator.next = linked_list
            linked_list_iterator=linked_list_iterator.next
            if linked_list.next:
                heapq.heappush(heap, (linked_list.next.val, linked_list.next))
               

        return merged_linked_list.next
