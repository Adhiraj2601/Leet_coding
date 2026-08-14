# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr=head
        l=0
        while curr:
            l+=1
            curr=curr.next
        fast = head
        for i in range(k-1):
            fast=fast.next
        first=fast
        slow=head
        while fast.next:
            slow=slow.next
            fast=fast.next
        second=slow
        temp = first.val
        first.val = second.val
        second.val = temp
        return head

        