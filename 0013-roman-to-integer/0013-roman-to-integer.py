class Solution:
    def romanToInt(self, s: str) -> int:
        dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        num=0
        i = 0
        while i<len(s):
            if i<len(s)-1:
                if s[i]=='I' and (s[i+1]=='V' or s[i+1]=='X'):
                    num+=dict[s[i+1]]-1
                    i+=2
                elif s[i]=='X' and (s[i+1]=='L' or s[i+1]=='C'):
                    num+=dict[s[i+1]]-10
                    i+=2
                elif s[i]=='C' and (s[i+1]=='D' or s[i+1]=='M'):
                    num+=dict[s[i+1]]-100
                    i+=2
                else:
                    num+=dict[s[i]]
                    i+=1
            else:
                num+=dict[s[i]]
                i+=1

        return num

            

            


        