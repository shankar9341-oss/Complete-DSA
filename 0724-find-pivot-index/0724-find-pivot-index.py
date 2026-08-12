class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftsum = 0
        totalsum = sum(nums)

        for i in range(len(nums)):
            rightsum = totalsum - nums[i] - leftsum\

            if leftsum == rightsum:
                return i
                
            leftsum += nums[i]
        return -1
        