class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total_sum = len(nums)*(len(nums) + 1)// 2
        result = sum(nums)
        return total_sum - result
