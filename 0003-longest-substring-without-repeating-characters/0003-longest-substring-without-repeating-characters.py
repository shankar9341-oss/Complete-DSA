class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        max_len = 0
        set1 = set()
        for right in range(len(s)):
            while s[right] in set1:
                set1.remove(s[left])
                left += 1

            key = (right - left + 1)
            max_len = max(max_len, key)
            set1.add(s[right])
        return max_len