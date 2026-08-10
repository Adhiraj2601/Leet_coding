# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        c = 0
        while curr:
            c+=1
            curr=curr.next
        curr = head
        c1 = 0
        req = c-n
        if req==0:
            return head.next
        while curr:
            c1+=1
            if c1==req:
                curr.next = curr.next.next
                break
            curr = curr.next
        return head
            


        