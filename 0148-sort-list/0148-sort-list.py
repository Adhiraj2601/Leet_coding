# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        min_heap=[]
        curr=head
        while curr:
            heapq.heappush(min_heap,curr.val)
            curr=curr.next
        curr=head
        while curr:
            curr.val = heapq.heappop(min_heap)
            curr=curr.next
        return head


        