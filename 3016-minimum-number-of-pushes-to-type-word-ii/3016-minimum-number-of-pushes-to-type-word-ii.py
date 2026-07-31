class Solution:
    def minimumPushes(self, word: str) -> int:
        freq = {}
        count = 0
        for i in word:
            if i not in freq:
                freq[i]=1
            else:
                freq[i]+=1
        sorted_freq = dict(sorted(freq.items(), key=lambda item: item[1], reverse=True))
        print(sorted_freq)
        k = 1
        c = 0
        for i in sorted_freq:
            count = count + sorted_freq[i]*k
            c+=1
            if c%8==0:
                k+=1
        
        return count


        