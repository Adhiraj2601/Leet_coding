# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr = head
        while curr!=None:
            if curr.val!="visited":
                curr.val="visited"
            else:
                return True
            curr = curr.next
        return False


        