class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_pro = min_pro = ans = nums[0]

        for i in range(1, len(nums)):
            if nums[i] < 0:
                max_pro, min_pro = min_pro, max_pro
            
            max_pro = max(nums[i], max_pro * nums[i])
            min_pro = min(nums[i], min_pro * nums[i])
            
            ans = max(ans, max_pro)
        return ans