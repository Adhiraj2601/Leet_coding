from typing import List

class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        # Helper function to compute area difference at height Y
        def area_diff(Y: float) -> float:
            below = 0.0
            above = 0.0
            
            for x, y, l in squares:
                bottom = y
                top = y + l
                total = l * l
                
                if top <= Y:
                    below += total
                elif bottom >= Y:
                    above += total
                else:
                    # Line cuts the square
                    below += l * (Y - bottom)
                    above += l * (top - Y)
            
            return below - above  # we want this to be 0

        # Binary search bounds
        low = min(y for _, y, _ in squares)
        high = max(y + l for _, y, l in squares)

        # Binary search for precision 1e-5
        while high - low > 1e-5:
            mid = (low + high) / 2
            if area_diff(mid) < 0:
                low = mid
            else:
                high = mid

        return low    