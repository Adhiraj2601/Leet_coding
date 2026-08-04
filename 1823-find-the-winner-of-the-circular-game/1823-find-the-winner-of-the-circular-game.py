class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        sample = list(range(1, n + 1))
        curr = 0 
        while len(sample) > 1:
            curr = (curr + k - 1) % len(sample)
            sample.pop(curr)
        return sample[0]


        
        