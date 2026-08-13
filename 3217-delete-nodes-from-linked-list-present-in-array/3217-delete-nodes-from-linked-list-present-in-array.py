# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums = set(nums)
        dummy = ListNode(0)
        durr = dummy
        curr = head
        while curr:
            if curr.val not in nums:
                durr.next = ListNode(curr.val)
                durr = durr.next
            curr = curr.next
                
        return dummy.next

        