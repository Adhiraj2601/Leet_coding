class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        curr = nums[0]
        p = 1
        for i in range(len(nums)):
            if curr!=nums[i]:
                nums[p]=nums[i]
                curr = nums[i]
                p+=1
        return p

            
        
        