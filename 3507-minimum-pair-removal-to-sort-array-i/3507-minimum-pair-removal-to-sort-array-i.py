class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        c=0
        pos=0
        while sorted(nums)!=nums:
            mi = float('inf')
            for i in range(len(nums)-1):
                s = nums[i]+nums[i+1]
                if s<mi:
                    mi = s
                    pos = i
            c+=1
            nums[pos]=mi
            del nums[pos+1]
        return c
            
