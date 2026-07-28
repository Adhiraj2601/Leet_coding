class Solution:
    def smallestPalindrome(self, s: str) -> str:
        l = len(s)
        if l==1:
            return s
        mid = l//2
        min_heap = []
        res  = ''
        for i in range(mid):
            heapq.heappush(min_heap,s[i])
        for i in range(mid):
            res+=heapq.heappop(min_heap)
        if l%2==0:
            res+=res[::-1]
        else:
            res+=s[mid]
            res+=res[:mid][::-1]
        return res

        