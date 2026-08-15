class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hash = {}
        
        for char in magazine:
            hash[char] = 1 + hash.get(char,0) 

        for char in ransomNote:
            if char not in hash or hash[char] <= 0:
                return False
            hash[char] -= 1
        return True