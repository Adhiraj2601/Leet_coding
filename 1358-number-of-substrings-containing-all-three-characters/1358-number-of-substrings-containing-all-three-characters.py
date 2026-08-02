class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        last = {'a': -1, 'b': -1, 'c': -1}
        total = 0
        
        for i, char in enumerate(s):
            last[char] = i
            min_index = min(last['a'], last['b'], last['c'])
            if min_index != -1:
                total += min_index + 1
                
        return total

        