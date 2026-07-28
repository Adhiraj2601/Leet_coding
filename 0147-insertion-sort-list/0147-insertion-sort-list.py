# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        vals = []
        curr = head
        while curr:
            vals.append(curr.val)
            curr = curr.next

        vals.sort()

        curr = head
        for val in vals:
            curr.val = val
            curr = curr.next

        return head