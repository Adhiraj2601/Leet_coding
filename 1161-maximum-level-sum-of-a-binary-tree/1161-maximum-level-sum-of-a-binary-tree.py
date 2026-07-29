class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        level = 1
        max_sum = float('-inf')
        answer = 1

        while q:
            size = len(q)
            current_sum = 0

            for _ in range(size):
                node = q.popleft()
                current_sum += node.val

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            if current_sum > max_sum:
                max_sum = current_sum
                answer = level

            level += 1

        return answer

        