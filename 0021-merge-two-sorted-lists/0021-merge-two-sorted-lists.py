# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        current = list1
        l1 = []
        while current:
            l1.append(current.val)
            current = current.next

        current = list2
        l2 = []
        while current:
            l2.append(current.val)
            current = current.next
      
        res = l1+l2
        res.sort()
        dummy = ListNode(0)
        curr = dummy
        for i in range(len(res)):
            curr.next = ListNode(res[i])
            curr = curr.next
        return dummy.next
            

        
            


        