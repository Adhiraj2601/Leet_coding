class Solution:
    def reverse(self, x: int) -> int:
        s = str(x)
        l = len(s)
        if x>=0:
            return int(s[::-1]) if int(s[::-1])<2**31 else 0
        else:
            return -int(s[1:l][::-1]) if -int(s[1:l][::-1])>-2**31 else 0
        