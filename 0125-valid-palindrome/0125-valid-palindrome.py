class Solution:
    def isPalindrome(self, s: str) -> bool:

        st = 0
        end = len(s)-1
     
        while st < end:
            if not s[st].isalnum():
                st += 1
            elif not s[end].isalnum():
                end -= 1
            else:
                if s[st].lower() != s[end].lower():
                    return False

                st += 1
                end -= 1
        return True
