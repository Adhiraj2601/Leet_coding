class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m = len(grid)
        c=0
        for i in range(m-1,-1,-1):
            for j in range(len(grid[i])-1,-1,-1):
                if grid[i][j]<0:
                    c+=1
                else:
                    break
        return c

        