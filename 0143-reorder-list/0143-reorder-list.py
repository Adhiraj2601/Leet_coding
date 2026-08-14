# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head: return None
        stack=[]
        l=0
        curr=head
        while curr:
            stack.append(curr)
            curr=curr.next
            l+=1
        nxt=head
        curr=head
        for i in range(l//2):
            nxt=curr.next
            curr.next=stack.pop()
            curr.next.next=nxt
            curr=nxt
        if nxt:
            nxt.next=None
        return head
