# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        curr=head.next
        prev=head
        nex = curr.next
        i=1
        c=0
        critical=[]
        min = float('inf')
        while curr and nex:
            if (prev.val>curr.val and curr.val<nex.val) or (prev.val<curr.val and curr.val>nex.val):
                critical.append(i)
                c+=1
            
            if len(critical)>1:
                d = critical[-1]-critical[-2]
                if d<min:
                    min = d
            
            prev = curr
            curr = curr.next
            nex = curr.next
            i+=1
        if c<2:
            return[-1,-1]
        else:
            return [min,critical[-1]-critical[0]]
            




        