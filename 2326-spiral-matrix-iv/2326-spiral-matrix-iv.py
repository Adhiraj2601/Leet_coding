# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        matrix = [[0] * n for _ in range(m)]
        top, bottom = 0, m - 1
        left, right = 0, n - 1
        curr=head
        while top <= bottom and left <= right:
            for j in range(left, right + 1):
                if curr is not None:
                    c = curr.val
                    curr = curr.next
                else:
                    c = -1
                matrix[top][j] = c
            top += 1

            for i in range(top, bottom + 1):
                if curr is not None:
                    c = curr.val
                    curr = curr.next
                else:
                    c = -1
                matrix[i][right] = c
            right -= 1

            if top <= bottom:
                for j in range(right, left - 1, -1):
                    if curr is not None:
                        c = curr.val
                        curr = curr.next
                    else:
                        c = -1
                    matrix[bottom][j] = c
                bottom -= 1
                
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    if curr is not None:
                        c = curr.val
                        curr = curr.next
                    else:
                        c = -1
                    matrix[i][left] = c
                left += 1

        return matrix