# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        minheap = []
        for head in lists:
           curr = head
           while curr:
            heapq.heappush(minheap, curr.val)
            curr=curr.next

        dummy = ListNode(0)
        curr = dummy
        for i in range(len(minheap)):
            curr.next = ListNode(heapq.heappop(minheap))
            curr = curr.next
        return dummy.next


        