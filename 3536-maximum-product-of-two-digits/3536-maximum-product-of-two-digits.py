class Solution:
    def maxProduct(self, n: int) -> int:
        s = str(n)
        l = []
        for i in s:
            l.append(int(i))
        l.sort(reverse = True)
        return (l[0]*l[1])


        