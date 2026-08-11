class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map1 = {}
        map2 = {}
        for char1,char2 in zip(s,t):
            if ((char1 in map1 and map1[char1] != char2) or
                (char2 in map2 and map2[char2] != char1)):
                return False

            map1[char1] = char2
            map2[char2] = char1
        return True