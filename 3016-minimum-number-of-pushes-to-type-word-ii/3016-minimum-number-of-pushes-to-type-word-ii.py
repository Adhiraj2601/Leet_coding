class Solution:
    def minimumPushes(self, word: str) -> int:
        counts = Counter(word).values()
        sorted_counts = sorted(counts, reverse=True)
        total_pushes = 0
        for i, freq in enumerate(sorted_counts):
            total_pushes += freq * (i // 8 + 1)
            
        return total_pushes

        