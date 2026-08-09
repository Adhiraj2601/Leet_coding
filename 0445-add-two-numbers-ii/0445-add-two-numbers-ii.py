# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy
        num1=''
        num2=''
        sum=0
        while l1:
            val1 = l1.val
            num1+=str(val1)
            l1 = l1.next
            
        while l2:
            val2 = l2.val
            num2+=str(val2)
            l2 = l2.next
            
        sum = int(num1)+int(num2)
        s = str(sum)
        for i in range(len(s)):
            curr.next = ListNode(int(s[i]))
            curr = curr.next

        return dummy.next
        