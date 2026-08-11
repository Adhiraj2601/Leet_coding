# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        curr = head
        dummy = ListNode(0)
        durr = dummy
        while curr:
            if curr.val<x:
                durr.next = ListNode(curr.val)
                durr = durr.next
            curr = curr.next
        curr = head
        while curr:
            if curr.val>=x:
                durr.next = ListNode(curr.val)
                durr=durr.next
            curr= curr.next
        return dummy.next
            


        