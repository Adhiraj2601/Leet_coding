class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        res = [[rStart, cStart]]
        total = rows * cols
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        r, c = rStart, cStart
        steps = 1  
        d = 0  # Direction index (0=East, 1=South, 2=West, 3=North)

        while len(res) < total:
            for _ in range(2):
                dr, dc = directions[d]
                for _ in range(steps):
                    r += dr
                    c += dc
                    if 0 <= r < rows and 0 <= c < cols:
                        res.append([r, c])
               
                d = (d + 1) % 4
            steps += 1  

        return res

        