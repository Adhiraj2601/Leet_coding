# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        curr = head
        stack=[]
        num=[]
        while curr:
            stack.append(curr.val)
            num.append(curr.val)
            curr=curr.next
        for i in range(len(num)):
            if num[i]!=stack.pop():
                return False
        return True
        