class Solution:
    def countTriples(self, n: int) -> int:
        c = 0
        for i in range(1,n+1):
            for j in range(i+1,n+1):
                sq = math.sqrt((i*i)+(j*j))
                if sq == int(sq) and sq<=n:
                    c+=2
                    print(i,j,c)
        return c