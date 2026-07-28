class Solution:
    def smallestPalindrome(self, s: str) -> str:
        n = len(s)
        half = "".join(sorted(s[: n // 2]))
        mid_char = s[n // 2] if n % 2 != 0 else ""

        return half + mid_char + half[::-1]

        