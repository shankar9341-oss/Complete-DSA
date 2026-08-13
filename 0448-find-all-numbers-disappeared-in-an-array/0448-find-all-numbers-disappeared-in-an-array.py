class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for n in nums:
            idx = abs(n) - 1
            if nums[idx] > 0:
                nums[idx] = -nums[idx]
        
        res = []
        for i,n in enumerate(nums):
            if n > 0:
                res.append(i + 1)
        return res