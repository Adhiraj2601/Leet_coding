# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head: return None
        if k==0: return head
        n=0
        curr=head
        while curr:
            n+=1
            if curr.next is None:
                tail = curr
            curr=curr.next
        k = k%n
        tail.next = head

        fast=head
        c = 0
        while fast:
            if c==n-k-1:
                new_tail = fast
                break
            fast = fast.next
            c+=1
        new_head = new_tail.next
        new_tail.next = None
        return new_head
      
            

        