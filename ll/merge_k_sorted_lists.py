# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        '''
 Since each list is already sorted, we only need to keep track of the smallest element across all k lists.
        '''
        # ListNode.__eq__ = lambda self, other: self.val==other
        # ListNode.__lt__ = lambda self, other:self.val<other
        # heap = []
        # merged_linked_list = ListNode()
        # linked_list_iterator = merged_linked_list

        # for index,linked_list in enumerate(lists):
        #     if linked_list:
        #         heapq.heappush(heap, (linked_list.val, linked_list))

        # while heap:
        #     val, linked_list = heapq.heappop(heap)
        #     linked_list_iterator.next = linked_list
        #     linked_list_iterator=linked_list_iterator.next
        #     if linked_list.next:
        #         heapq.heappush(heap, (linked_list.next.val, linked_list.next))
               

        # return merged_linked_list.next
        def merge_list(l1, l2):
            dummy = ListNode(0)
            cur = dummy
            while l1 and l2:
                if l1.val<=l2.val:
                    cur.next = l1
                    l1 = l1.next
                else:
                    cur.next = l2
                    l2 = l2.next
                cur = cur.next
            if l1:
                cur.next = l1
            if l2:
                cur.next = l2
            return dummy.next
        if not lists:
            return
        while len(lists)>1:
            merged_lists = []
            for idx in range(0, len(lists), 2):
                if idx+1<len(lists):
                    merged_lists.append(merge_list(lists[idx], lists[idx+1]))
                else:
                    merged_lists.append(lists[idx])
            lists = merged_lists
        return lists[0]

        