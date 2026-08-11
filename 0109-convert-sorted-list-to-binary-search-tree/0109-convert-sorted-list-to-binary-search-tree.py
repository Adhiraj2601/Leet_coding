# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if head is None:return None
        nums=[]
        while head:
            nums.append(head.val)
            head = head.next
        l = len(nums)
 
        def build_tree(left:int, right:int):
            if left>right:
                return None
            mid = (left+right)//2
            root = TreeNode(nums[mid])

            root.left=build_tree(left,mid-1)
            root.right=build_tree(mid+1,right)
            return root
        return build_tree(0,l-1)

