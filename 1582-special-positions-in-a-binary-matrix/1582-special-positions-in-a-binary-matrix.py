class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:

        rsum = [sum(row) for row in mat]
        csum = [sum(col) for col in zip(*mat)]
        
        special_count = 0

        for r in range(len(mat)):
            for c in range(len(mat[0])):
                if mat[r][c] == 1:
                    if rsum[r] == 1 and csum[c] == 1:
                        special_count += 1
                        
        return special_count