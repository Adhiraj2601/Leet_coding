class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        flip_count = 0
        while k > 1:
            middle = 2**(n - 1)
            if k == middle:
                return str(1 ^ (flip_count % 2))
            if k > middle:
                k = 2 * middle - k
                flip_count += 1
            n -= 1
        return str(0 ^ (flip_count % 2))
    