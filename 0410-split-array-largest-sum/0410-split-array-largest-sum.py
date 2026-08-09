class Solution:
    def splitArray(self, nums, k):
        left = max(nums)
        right = sum(nums)
        res = right
        while left <= right:
            mid = (left + right) // 2
            if self.split(nums, k, mid):
                res = mid
                right = mid - 1
            else:
                left = mid + 1
        return res
    
    def split(self, nums, k, max_sum):
        curr_sum = 0
        count = 1
        for n in nums:
            if curr_sum + n <= max_sum:
                curr_sum += n
            else:
                count += 1
                curr_sum = n
        return count <= k
