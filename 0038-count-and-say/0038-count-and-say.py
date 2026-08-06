class Solution:
    def countAndSay(self, n: int) -> str:
        if n==1:
            return "1"
        else:
            return self.count(self.countAndSay(n-1)) 
    def count(self, n: str) -> str:
        res=''
        c=1
        for i in range(len(n)-1):
            if n[i]==n[i+1]:
                c+=1
            else:
                res+=str(c)+n[i]
                c=1
        res+=str(c)+n[-1]
        return res



        
        