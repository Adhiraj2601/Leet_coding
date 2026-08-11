# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if head is None:return None
        if head.next is None:return head
        curr = head
        c = 1
        stack=[]
        while curr:
            if c>=left and c<=right:
                stack.append(curr.val)
            curr = curr.next
            c+=1
        curr = head
        c=1
        while curr:
            if c>=left and c<=right:
                curr.val = stack.pop()
            curr = curr.next
            c+=1
        return head
        

        