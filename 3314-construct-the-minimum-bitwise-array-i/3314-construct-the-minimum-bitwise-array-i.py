class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        res = []
        for n in nums:
            t = 0
            x = n
            while x & 1:
                t += 1
                x >>= 1
            if t == 0:
                res.append(-1)
            else:
                res.append(n - (1 << (t - 1)))
        return res

