class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        l = len(nums)
        nums.sort()
        closest_sum = nums[0]+nums[1]+nums[2]
        for i in range(l-2):
            left = i+1
            right = l-1
            while left<right:
                curr_sum = nums[i]+nums[left]+nums[right]
                if abs(curr_sum - target) < abs(closest_sum-target):
                    closest_sum = curr_sum
            
                if curr_sum==target:
                    return curr_sum
                elif curr_sum<target:
                    left+=1
                else:
                    right-=1
         
        return closest_sum



        