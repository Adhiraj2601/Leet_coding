# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None: return None
        curr=head
        stack = []
        while curr:
            while stack and curr.val>stack[-1]:
                stack.pop()
            stack.append(curr.val)
            curr=curr.next
        dummy = ListNode(0)
        curr=dummy
        for i in range(len(stack)):
            curr.next = ListNode(stack[i])
            curr=curr.next
        return dummy.next


            