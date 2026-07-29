class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        s = 0
        neg = 0 
        mi = 10**5
        
        for i in matrix:
            for j in i:
                if j<0:
                    neg+=1
                aj = abs(j)
                if aj<mi:
                    mi=aj
                s = s + aj
        if neg%2==0:
            return s
        else:
            print(s, mi)
            return s - (2*mi)
            
        