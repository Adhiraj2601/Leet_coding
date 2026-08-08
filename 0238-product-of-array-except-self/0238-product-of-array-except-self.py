class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        prefix = []
        suffix = [0]*l
        prod=1
        for i in range(l):
            prefix.append(prod)
            prod = nums[i]*prod
        prod =1
        for i in range(l-1,-1,-1):
            suffix[i]=prod
            prod = nums[i]*prod    
        for i in range(l):
            nums[i] = prefix[i]*suffix[i]
        return nums
        