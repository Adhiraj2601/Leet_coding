# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        curr=head
        stack=[]
        l = 0
        max = -1
        while curr:
            stack.append(curr.val)
            l+=1
            curr=curr.next
        curr=head
        for i in range(l//2):
            s = curr.val+stack.pop()
            if s>max:
                max=s
            curr=curr.next
        stack=[]
        return max



