class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        ma = 0
        for i in range(int(len(nums)/2)):
            s = nums[i]+nums[-i-1]
            if s>ma:
                ma=s
        return ma
        