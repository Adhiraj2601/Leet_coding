class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        l = len(arr)
        arr2 = [0]*l
        for i in range(l):
            b = (bin(arr[i])[2:])
            arr2[i] = [b.count('1'), arr[i]]
        arr2.sort()
        for i in range(l):
            arr2[i] = arr2[i][1]
        return arr2
        
        
            
        