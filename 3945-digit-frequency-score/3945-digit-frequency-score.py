class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        n = str(n)
        d = {}
        score=0
        for i in n:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        for num,freq in d.items():
            score+=(int(num)*freq)
        return score
