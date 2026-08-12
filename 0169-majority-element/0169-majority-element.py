class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        my_dict = {}
        for i in range(len(nums)):
            if nums[i] not in my_dict:
                my_dict[nums[i]]=1
            else:
                my_dict[nums[i]]+=1
        l = len(nums)/2
        for key, value in my_dict.items():
            if value>l:
                return key
           
        