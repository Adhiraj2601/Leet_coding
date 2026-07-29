class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        s = 0
        for i in nums:
            t=[]
            for j in range(1,int(math.sqrt(i))+1):
                if i%j==0:
                    t.append(j)
                    d = int(i/j)
                    if d!=j:
                        t.append(d)
            if len(t)==4:
                s = sum(t) + s
        return s




        