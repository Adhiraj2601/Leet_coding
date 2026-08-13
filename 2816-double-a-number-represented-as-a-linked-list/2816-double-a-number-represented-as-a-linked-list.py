# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack=[]
        curr = head
        while curr:
            stack.append(curr.val)
            curr=curr.next
        num=[]
        carry = 0
        while stack:
            n = stack.pop()*2
            res = n%10
            num.append(res+carry)
            carry = n//10
        if carry!=0:
            num.append(carry)
        dummy = ListNode(0)
        curr= dummy
        while num:
            curr.next = ListNode(num.pop())
            curr=curr.next
        return dummy.next            


        