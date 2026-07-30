class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: list[int], vFences: list[int]) -> int:
        MOD = 10**9 + 7

        h = sorted([1] + hFences + [m])
        v = sorted([1] + vFences + [n])

        H = set()
        for i in range(len(h)):
            for j in range(i + 1, len(h)):
                H.add(h[j] - h[i])
        
        V = set()
        for i in range(len(v)):
            for j in range(i + 1, len(v)):
                V.add(v[j] - v[i])

        possible = H & V
        if not possible:
            return -1
        
        side = max(possible)
        return (side * side) % MOD
