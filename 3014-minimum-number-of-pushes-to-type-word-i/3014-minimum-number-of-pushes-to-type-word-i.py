class Solution:
    def minimumPushes(self, word: str) -> int:
        l = len(word)
        c=0
        i=1
        while l!=0:
            if l<=8:
                return c+(l*i)
            else:
                c= c+(i*8)
                i+=1
                l-=8
        
            
                


            
        