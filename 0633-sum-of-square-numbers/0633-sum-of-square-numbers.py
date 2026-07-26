class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        start = 0
        end = int(math.sqrt(c))
        while start<=end:
            if (start*start) + (end*end) == c:
                return True
            elif (start*start) + (end*end) > c:
                end-=1
            else:
                start+=1
        return False
        