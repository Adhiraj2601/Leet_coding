# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None: return None
        dummy = ListNode(0)
        curr = dummy
        org = head
        tail = head
        prev = org.val
        org = org.next
        c=0
        while org:
            if org.val == prev:
                c+=1
            else:
                if c==0:
                    curr.next = ListNode(prev)
                    curr = curr.next
                prev = org.val
                c=0
            if org.next==None:
                tail = org
            org = org.next

        if c==0:
            curr.next = ListNode(tail.val)   
        return dummy.next

            
        