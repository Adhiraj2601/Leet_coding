class Solution:

    def divide(self, dividend: int, divisor: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        if dividend == divisor:
            return 1

        is_positive = (dividend < 0) == (divisor < 0)

        a = abs(dividend)
        b = abs(divisor)
        ans = 0

        while a >= b:
            q = 0
            while a >= (b << (q + 1)):
                q += 1

            ans += 1 << q
            a -= b << q

        res = ans if is_positive else -ans

        if res > INT_MAX:
            return INT_MAX
        if res < INT_MIN:
            return INT_MIN

        return res

        