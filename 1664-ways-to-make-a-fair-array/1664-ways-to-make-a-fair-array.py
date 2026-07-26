class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        e_sum = 0
        o_sum =0
        c = 0
        c_even = 0
        c_odd = 0
        for i in range(len(nums)):
            if i%2==0:
                e_sum+=nums[i]
            else:
                o_sum+=nums[i]
        
        for i in range(len(nums)):
            if i%2==0:
                e_sum -= nums[i]
            else:
                o_sum -= nums[i]
    
            if c_odd+e_sum == c_even+o_sum:
                c+=1

            if i%2==0:
                c_even+=nums[i]
            else:
                c_odd+=nums[i]
        return c
            
                

            