class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort(key=len)
        start = strs[0]
        s=''
        c=1
        for i in range(len(start)):
            for j in range(1,len(strs)):
                if start[i]==strs[j][i]:
                    c+=1

            if c==len(strs):
                s+=start[i]
            else:
                break
            c=1
        return s

                
                
        