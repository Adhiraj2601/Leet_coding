class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        
        _sign = True
        
        if divisor < 0 and dividend > 0:
            _sign = False
        if dividend < 0 and divisor > 0:
            _sign = False

        dividend = abs(dividend)
        divisor = abs(divisor)
        i = 0
        q = 0
        while dividend >= divisor:
            
            if dividend < divisor<<i:
                i = 0

            dividend -= divisor<<i
            q += 1<<i
            i += 1
            

        if not _sign:
            return max(-q, pow(-2, 31))
        return min(q, pow(2, 31)-1)
        