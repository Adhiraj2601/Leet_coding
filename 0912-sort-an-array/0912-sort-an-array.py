class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        min_val = min(nums)
        max_val = max(nums)
        k = max_val - min_val + 1

        count = [0] * k
        output = [0] * len(nums)

        for num in nums:
            count[num - min_val] += 1

        for i in range(1, k):
            count[i] += count[i - 1]

        for num in reversed(nums):
            idx = count[num - min_val] - 1
            output[idx] = num
            count[num - min_val] -= 1

        return output