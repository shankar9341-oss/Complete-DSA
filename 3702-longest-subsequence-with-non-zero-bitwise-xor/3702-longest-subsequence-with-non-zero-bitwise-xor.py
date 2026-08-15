class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        xor = 0
        count_zero = 0
        for n in nums:
            xor ^= n
            if n == 0:
                count_zero += 1
        if xor == 0:
            if count_zero == len(nums):
                return 0
            return len(nums) - 1
        return len(nums)
