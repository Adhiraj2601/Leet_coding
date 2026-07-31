class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        sum = nums[0]
        nums.remove(sum)
        for i in range(2):
            sum+=min(nums)
            nums.remove(min(nums))
        return sum