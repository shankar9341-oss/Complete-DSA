class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sett = set(nums)
        longest = 0
        for num in sett:
            if num - 1 not in sett:
                count = 1
                while num + 1 in sett:
                    count += 1
                    num += 1
                longest = max(longest, count)
        return longest