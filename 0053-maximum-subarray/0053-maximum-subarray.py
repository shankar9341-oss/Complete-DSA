class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # max_sum = nums[0]
        # curr_sum = 0
        # for i in range(len(nums)):
        #     curr_sum = max(nums[i],curr_sum + nums[i])
        #     max_sum = max(max_sum,curr_sum)  
                
        # return max_sum


        max_sum = float("-Inf")
        sum1 = 0
        for n in nums:
            sum1 += n
            if sum1 > max_sum:
                max_sum = sum1
            if sum1 < 0:
                sum1 = 0
        return max_sum

            