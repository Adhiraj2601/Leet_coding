class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        mi=(100000)+1
        for i in range(len(nums)-k+1):
            dif = nums[i+k-1]-nums[i]
            if dif<mi:
                mi=dif
        return mi


        