# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        current1 = l1
        len1=0
        while current1 is not None:
            len1+=1
            current1 = current1.next

        current2 = l2
        len2=0
        while current2 is not None:
            len2+=1
            current2 = current2.next

        if len1<len2:
            max = l2
            min = l1
        else:
            max = l1
            min = l2

        dummy = ListNode(0)
        curr=dummy
        carry = 0

        while min is not None:
            current = int((max.val+min.val+carry)%10)

            curr.next = ListNode(current)
            curr=curr.next

            carry = int((max.val+min.val+carry)/10)

            max = max.next
            min = min.next
        while max is not None:
            current = int((max.val+carry)%10)

            curr.next = ListNode(current)
            curr=curr.next

            carry = int((max.val+carry)/10)

            max = max.next
        if carry>0:
            curr.next = ListNode(carry)
      
        return dummy.next
            

            
        
        
        
        
     
    
        
        

        