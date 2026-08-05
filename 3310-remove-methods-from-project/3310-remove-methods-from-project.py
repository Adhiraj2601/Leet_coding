from collections import deque
from typing import List

class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(n)]
        for u, v in invocations:
            graph[u].append(v)

        is_suspicious = [False] * n
        is_suspicious[k] = True
        queue = deque([k])
        
        while queue:
            curr = queue.popleft()
            for neighbor in graph[curr]:
                if not is_suspicious[neighbor]:
                    is_suspicious[neighbor] = True
                    queue.append(neighbor)
        can_remove = True
        for u, v in invocations:
            if is_suspicious[v] and not is_suspicious[u]:
                can_remove = False
                break

        if can_remove:
            return [i for i in range(n) if not is_suspicious[i]]
        else:
            return list(range(n))
        