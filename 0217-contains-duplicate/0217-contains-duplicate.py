class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # return len(set(nums)) != len(nums)
        sett = set()
        for i in nums:
            if i in sett:
                return True
            sett.add(i)
        return False