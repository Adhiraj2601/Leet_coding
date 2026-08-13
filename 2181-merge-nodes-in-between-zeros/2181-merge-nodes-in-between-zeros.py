# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sum = 0
        curr = head.next
        prev = head
        while curr:
            if curr.val!=0:
                sum+=curr.val
                prev.next=curr.next
                curr=curr.next

            else:
                curr.val=sum
                sum=0
                prev = curr
                curr=curr.next
        return head.next
