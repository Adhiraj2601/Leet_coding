class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        MOD = 10**9 + 7
        from collections import defaultdict
        levels = defaultdict(int)
        for x, y in points:
            levels[y] += 1
        segcount = []
        for y, k in levels.items():
            if k >= 2:
                segcount.append(k * (k - 1) // 2)
        segcount.sort()
        ans = 0
        pref = 0
        for s in segcount:
            ans = (ans + pref * s) % MOD
            pref = (pref + s) % MOD
        return ans






