class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k=1
        for i in range(1, len(nums)):
            if nums[i]==nums[i-1]:
                nums[i-1]=101
            else:
                k+=1
        nums.sort()
        return k
        
        