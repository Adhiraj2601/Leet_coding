# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:return None
        curr= head
        while curr and curr.next:
            first = curr
            second = curr.next
            gcd = ListNode(math.gcd(first.val,second.val))
            gcd.next = second
            first.next = gcd
            curr = curr.next.next
        return head
        