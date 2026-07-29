class Solution:
    def countOdds(self, low: int, high: int) -> int:
        range = high-low+1
        if range%2==0 or low%2==0:
            return int(range/2)
        
        else:
            return (int(range/2)+1)
        