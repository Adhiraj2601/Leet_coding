# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        prev=dummy
        curr=dummy.next
        while curr:
            if curr.val==val:
                prev.next=curr.next
                curr.next = prev.next

            else:
                prev=curr
            curr=curr.next
        return dummy.next
                
