class Solution:
    def smallestPalindrome(self, s: str) -> str:
        l = len(s)
        if l==1:
            return s
        mid = l//2
        res  = ''
        res = "".join(sorted(s[:mid]))
        if l%2==0:
            res+=res[::-1]
        else:
            res+=(s[mid]+res[:mid][::-1])
        return res

        