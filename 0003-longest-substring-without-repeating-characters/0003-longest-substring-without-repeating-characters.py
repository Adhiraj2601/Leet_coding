class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        max_len=0
        dict = {}
        for right in range(len(s)):
            if s[right] not in dict:
                dict[s[right]]=right
            else:
                d = right-left
                left = max(left, dict[s[right]] + 1)
                
            dict[s[right]]=right
            max_len = max(max_len, right - left + 1)
        return max_len

            



            
        