class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []
        for p in nums:
            t = 0
            x = p
            while x & 1:
                t += 1
                x >>= 1

            if t == 0:
                ans.append(-1)
            else:
                ans.append(p - (1 << (t - 1)))
        return ans

        