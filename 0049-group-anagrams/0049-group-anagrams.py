class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mpp = defaultdict(list)
        result = []
        for s in strs:
            sort = tuple(sorted(s))
            mpp[sort].append(s)
        
        for value in mpp.values():
            result.append(value)
        
        return result

