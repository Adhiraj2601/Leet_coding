class Solution:
    def magicalString(self, n: int) -> int:
        if n<=3:
            return 1
        s =[1,2,2]
        i = 2
        while i<n:
            if s[i]==2 and s[-1]==1:
                s.append(2)
                s.append(2)
            elif s[i]==2 and s[-1]==2:
                s.append(1)
                s.append(1)
            elif s[i]==1 and s[-1]==1:
                s.append(2)
            elif s[i]==1 and s[-1]==2:
                s.append(1)
            i+=1
        return s[:n].count(1)
        
            
