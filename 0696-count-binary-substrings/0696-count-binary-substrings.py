class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        sum = 0
        c = 1
        size = []
        for i in range(1,len(s)):
            if s[i] == s[i-1]:
                c+=1
            else:
                size.append(c)
                c=1
        size.append(c)

        for i in range(len(size)-1):
            sum = sum + min(size[i],size[i+1])
        
        return sum


        