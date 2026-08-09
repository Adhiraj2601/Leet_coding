class Solution:
    def minOperations(self, s: str) -> int:
        startone = ("10"*((len(s)//2)+1))
        startzero = ("01"*((len(s)//2)+1))
        cone = 0
        czero = 0
        cone = sum(c1 != c2 for c1, c2 in zip(startone, s))
        
        czero = sum(c1 != c2 for c1, c2 in zip(startzero, s))
        if cone>czero:
            return czero
        else:
            return cone
        