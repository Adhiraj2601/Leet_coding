class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k%len(nums)
        start = len(nums)-k
        temp=[]
        for i in range(start):
            temp.append(nums[i])
        j=0   
        for i in range(len(nums)-len(temp)):
            nums[i]=nums[start]
            start+=1
            j = i+1
        k=0
        for i in range(j,len(nums)):
            nums[i]=temp[k]
            k+=1
       