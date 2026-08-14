# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        first=headA
        second=headB
        while first or second:
            if first==None:
                first=headB
            if second==None:
                second=headA
            if first==second:
                return first
            first=first.next
            second=second.next
        return None
        