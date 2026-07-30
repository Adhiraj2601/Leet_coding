class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: list[int], vBars: list[int]) -> int:
        
        def max_gap(bars):
            bars.sort()
            longest = 0
            current = 0
            
            for i in range(len(bars)):
                if i == 0 or bars[i] != bars[i - 1] + 1:
                    current = 1
                else:
                    current += 1
                longest = max(longest, current)
            
            return longest + 1  
        
        max_h = max_gap(hBars)
        max_v = max_gap(vBars)
        
        side = min(max_h, max_v)
        return side * side

        