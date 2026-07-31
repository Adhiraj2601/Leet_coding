class Solution:
    def minimumCost(self, source: str, target: str,
                    original: list[str], changed: list[str], cost: list[int]) -> int:
        INF = 10**18

        # Map strings to indices
        nodes = {}
        idx = 0
        for s in original + changed:
            if s not in nodes:
                nodes[s] = idx
                idx += 1

        m = idx
        dist = [[INF] * m for _ in range(m)]
        for i in range(m):
            dist[i][i] = 0

        for o, c, w in zip(original, changed, cost):
            u, v = nodes[o], nodes[c]
            dist[u][v] = min(dist[u][v], w)

        # Floyd–Warshall
        for k in range(m):
            for i in range(m):
                if dist[i][k] == INF:
                    continue
                for j in range(m):
                    nd = dist[i][k] + dist[k][j]
                    if nd < dist[i][j]:
                        dist[i][j] = nd

        # Only try lengths that actually exist
        valid_lengths = set(len(s) for s in original)

        n = len(source)
        dp = [INF] * (n + 1)
        dp[n] = 0

        for i in range(n - 1, -1, -1):
            if source[i] == target[i]:
                dp[i] = dp[i + 1]

            for L in valid_lengths:
                j = i + L
                if j > n:
                    continue
                x = source[i:j]
                y = target[i:j]
                if x in nodes and y in nodes:
                    u, v = nodes[x], nodes[y]
                    if dist[u][v] < INF:
                        dp[i] = min(dp[i], dist[u][v] + dp[j])

        return -1 if dp[0] == INF else dp[0]

