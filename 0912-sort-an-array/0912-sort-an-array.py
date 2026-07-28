class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if not nums:
            return nums
        min_val, max_val = min(nums), max(nums)
        k = max_val - min_val + 1
        count = [0] * k
        for num in nums:
            count[num - min_val] += 1

        idx = 0
        for val_idx in range(k):
            val = val_idx + min_val
            while count[val_idx] > 0:
                nums[idx] = val
                idx += 1
                count[val_idx] -= 1

        return nums