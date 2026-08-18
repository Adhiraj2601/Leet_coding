# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head: return None
        dummy = ListNode(0)
        durr = dummy

        curr = head
        c = 0
        
        h = head
        durr_tail = head
        while curr:
            c+=1
            if c==k:
                c=0
                prev  = curr.next
                for _ in range(k):
                    nxt = h.next
                    h.next = prev
                    prev = h
                    h = nxt
                durr.next=prev
                durr = durr_tail
                durr_tail = h
                curr = h
            else:
                curr = curr.next
        return dummy.next

    

                