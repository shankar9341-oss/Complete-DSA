class Solution:
    def reverseVowels(self, s: str) -> str:
        vol = set("aeiouAEIOU")
        left = 0
        right = len(s) - 1
        s = list(s)
        while left < right:
            if s[left] not in vol:
                left += 1
            elif s[right] not in vol:
                right -= 1
            else:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1

        return "".join(s)